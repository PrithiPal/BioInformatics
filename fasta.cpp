#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <unistd.h>
#include <iostream>
#include <string>
#include <map>

using namespace std;

typedef map<std::string, long> fmap_t;

fmap_t fasta_map;
FILE *fasta_file;

int
build_fasta_idx(char *tname)
{
    FILE *fidx = NULL;
    char *p, *t;
    long offset;
    int ret = 0;
    char tbuf[64048];

    fidx = fopen(tname, "w");
    if (fidx == NULL) {
        perror(tname);
        return(-1);
    }
    fseek(fasta_file, 0, SEEK_SET);
    while (fgets(tbuf, sizeof(tbuf), fasta_file)) {   
        if (strlen(tbuf) == sizeof(tbuf) - 1) {
            printf("XXX too long %s\n", tbuf);
            unlink(tname);
            ret = -2;
            break;
        }
        if (strncmp(tbuf, ">IPI:IPI", 4) == 0) {
            p = strchr(tbuf, '.');
            if (p == NULL) {
                p = strchr(tbuf, '|');
            }
            if (p == NULL) {
                printf("XXX %s", tbuf);
                unlink(tname);
                ret = -2;
                break;
            }
            *p = 0;
            p = tbuf + 5;
        } else if (strncmp(tbuf, ">sp|", 4) == 0) {
            p = strchr(tbuf + 4, '|');
            if (p == NULL) {
                printf("XXX %s", tbuf);
                unlink(tname);
                ret = -2;
                break;
            }
            *p = 0;
            p = tbuf + 4;
        } else {
            continue;
        }

        offset = ftell(fasta_file);
        fprintf(fidx, "%s %ld\n", p, offset);
    }

out:
    if (fidx != NULL) {
        fclose(fidx);
    }
    return ret;
}

int
load_fasta_idx(char *fname)
{
    struct stat st;
    char tname[256];
    FILE *fidx;
    long offset;
    char ipiname[20];
    char tbuf[2048];

    snprintf(tname, sizeof(tname), "%s.idx", fname);
    if (stat(tname, &st) < 0) {
        printf("build fasta idx file: %d \n",
                build_fasta_idx(tname));
    }

    fidx = fopen(tname, "r");
    if (fidx == NULL) {
        perror(tname);
        return(-1);
    }


    while (fgets(tbuf, sizeof(tbuf), fidx)) {
        if (sscanf(tbuf, "%s %ld", ipiname, &offset) == 2) {
            fasta_map[ipiname] = offset;
        } else {
            printf("XXX %s\n", tbuf);
        }
    }
    return 0;
}

int
read_ipi_seq(char *name, char *b, int bs)
{
    int l = 0, n= 0;
    fmap_t::iterator it;
    long off;
    char *p;

    it = fasta_map.find(name);
    if (it == fasta_map.end()) {
        return 0;
    }
    off = it->second;

    fseek(fasta_file, off, SEEK_SET);
    
    while ((p=fgets(b, bs - n, fasta_file)) != NULL) {
        if (!isalpha(*b) || !isupper(*b)) {
            break;
        }
        l = strlen(b);
        while (!isalpha(b[l-1])) {
            l--;
        }
        b += l;
        n += l;
    }
    if (p == NULL && !feof(fasta_file)) {
        printf("XXX %s too long > %d!\n", name, n);
    }
    return n;
}

int
main(int argc, char *argv[])
{
    char *fasta_name = NULL;
    int i = 1;
    long l;
    char tbuf[50000];

    if (argc < 2) {
        printf("usage:\n%s --fasta=<fasta_file> [sp/ipi_name] ...\n", argv[0]);
        exit(0);
    }

    while (i < argc) {
        if (*argv[i] !=  '-') {
            break;
        }
        if (strncmp(argv[i], "--fasta=", 8) == 0) {
            fasta_name = argv[i] + 8;
        }
        i++;
    }

    if (fasta_name != NULL) {
        fasta_file = fopen(fasta_name, "r");
        if (fasta_file == NULL) {
            perror(fasta_name);
            exit(-1);
        }
    } else {
        exit(0);
    }

    load_fasta_idx(fasta_name);

    while (i < argc) {
        l = read_ipi_seq(argv[i], tbuf, sizeof(tbuf));
        cout << "reading" << endl;
        tbuf[l] = 0;
        printf("%s\t%s\n", argv[i], tbuf);
        i++;
    }

    if (fasta_file != NULL) {
        fclose(fasta_file);
    }
}
