
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;
const int MAXLINE_LEN = 4096;

//STRUCTS used to store all the input data


struct n_glycos_input
{
	char *ipi;
	char *desc;
	int prot_len;
	int num_sequons;
	char *sequon_list;
};

struct trans_loop_input
{
	char *ipi;
	char *desc;
	char *loop_info;
	char *loop_len_info;
};

struct program_output
{
	char *ipi_gly, *ipi_ts;					//ipi index number
	char *desc_gly, *desc_ts;					//description
	int prot_len;				//length of protein 
	int num_sequons;			//number of NxS/T sequons in the protein
	char *sequon_list;			//list of NxS/T sequons present in protein
	char *loop_info;			//TMHMM Topology
	char *loop_len_info;		//length of each loop
	char *loop_final_info;		//final loop info
};

//Vectors to store all the input data (collection of STRUCTS from above)
vector<n_glycos_input> n_glycos_storage;
vector<trans_loop_input> trans_loop_storage;
vector<program_output> program_output_storage;

void add_final_loop_info()
{
	char *final_loop;

	for(int i = 0; i < program_output_storage.size(); i++)
	{
		final_loop = strrchr(program_output_storage.at(i).loop_info, '-');

		if(!final_loop)
			continue;

		char c = 0;
		int final;

		if(sscanf(final_loop, "-%d%c", &final, &c) == 2)
		{
			//check here for size!
			if(program_output_storage.at(i).prot_len - final < 0)
			{
				asprintf(&program_output_storage.at(i).loop_final_info, ", NO FINAL LOOP DATA-INCORRECT PROTEIN LENGTH");
				continue;
			}
			//printf("%s\n%c\n%d\n", program_output_storage.at(i).loop_info, c, final);
			asprintf(&program_output_storage.at(i).loop_final_info, ", %c(%d-%d=%d)", c, final, program_output_storage.at(i).prot_len, program_output_storage.at(i).prot_len - final);
			
			continue;
		}

		asprintf(&program_output_storage.at(i).loop_final_info, "ERROR-INCORRECT LOOP INFO\n");

	}

}

void match_and_store_output(n_glycos_input gly, trans_loop_input ts)
{
	program_output prog;
	prog.ipi_gly = strdup(gly.ipi);
	prog.ipi_ts = strdup(ts.ipi);
	prog.desc_gly = strdup(gly.desc);
	prog.desc_ts = strdup(ts.desc);
	prog.prot_len = gly.prot_len;
	prog.num_sequons = gly.num_sequons;
	prog.sequon_list = strdup(gly.sequon_list);
	prog.loop_info = strdup(ts.loop_info);
	prog.loop_len_info = strdup(ts.loop_len_info);
	prog.loop_final_info = NULL;
	program_output_storage.push_back(prog);
}

void find_common_proteins()
{
	for(int i = 0; i < trans_loop_storage.size(); i++)
	{
		for(int j = 0; j < n_glycos_storage.size(); j++)
		{
			if(strcmp(trans_loop_storage.at(i).ipi, n_glycos_storage.at(j).ipi) == 0)
            {
					match_and_store_output(n_glycos_storage.at(j), trans_loop_storage.at(i));
			}
		}
	}


}


void print_program_output()
{

	printf("IPI\tDescripion\tProtein Length\tNumber of Sequons\tSequon List\tTMHMM Topology\tTransmembrane Loop Length(s)\n");
	for(int i = 0; i < program_output_storage.size(); i++)
	{
	  /*	printf("%s\t%s\t%d\t%d\t%s\t%s\t%s%s\n", program_output_storage.at(i).ipi_ts, program_output_storage.at(i).desc_gly, program_output_storage.at(i).prot_len, 
			program_output_storage.at(i).num_sequons, program_output_storage.at(i).sequon_list, program_output_storage.at(i).loop_info, program_output_storage.at(i).loop_len_info,
			program_output_storage.at(i).loop_final_info); */

	    printf("%s\t%s\t%d\t%d\t%s\t%s\t%s\n", program_output_storage.at(i).ipi_ts, program_output_storage.at(i).desc_gly, program_output_storage.at(i).prot_len, 
			program_output_storage.at(i).num_sequons, program_output_storage.at(i).sequon_list, program_output_storage.at(i).loop_info, program_output_storage.at(i).loop_len_info); 

	}
}

bool process_trans_loop_line(char *new_line,char *organism_type)
{
	char *ipi, *desc, *loop_info, *loop_len_info;
	char *store1, *store2, *store3, *store4, *store5, *store6;
	//printf("%s\n",new_line);
	//ipi = strtok(new_line, "\t");
    
    //code by Prithi start
    if(strcmp(organism_type,"1") == 0) // human_trans_file
    {
       
    char *piece;
    piece = strtok (new_line,"|\t");
    piece = strtok (NULL,"|\t");
    int counter = 0;
    while(piece!=NULL)
    {
        if(counter==0){
            ipi = piece;
            
        }
        else if(counter == 2)
        {
            desc = piece;
        }
        else if(counter == 3)
        {
            loop_info = piece;
        }
        else if(counter == 4)
        {
            loop_len_info = piece;
        }
     piece = strtok (NULL,"\t");
        counter++;
    } // while end

    }
    else   // mouse_trans_file
    {;
        ipi = strtok(new_line, "\t");
        desc = strtok(NULL, "\t");
        loop_info = strtok(NULL, "\t");
        loop_len_info = strtok(NULL, "\t");

    }

 //code by Prithi end

	//	loop_len_info = strtok(NULL, "\n");
	
	store1 = strtok(NULL, "\t");
	store2 = strtok(NULL, "\t");
	store3 = strtok(NULL, "\t");
	store4 = strtok(NULL, "\t");
	store5 = strtok(NULL, "\t");
	store6 = strtok(NULL, "\n");
  //  cout << "trans ipi" << ipi << " trans desc = " << desc << " trans loop_info" << loop_info << " tran loop_len_info " << loop_len_info << endl;commentbyme
	//here I need to store other random information which I wont use

	if(ipi && desc && loop_info && loop_len_info)
    {
		trans_loop_input trans;

		trans.ipi = strdup(ipi);
		trans.desc = strdup(desc);
		trans.loop_info = strdup(loop_info);
		trans.loop_len_info = strdup(loop_len_info);

		trans_loop_storage.push_back(trans);
        
		return true;
	}

	return false;
}

bool process_n_glycos_output(char *new_line)
{
	char *ipi, *description, *sequon_list, *num_seq, *prot_len;

	ipi = strtok(new_line, "\t");
	description = strtok(NULL, "\t");
	prot_len = strtok(NULL, "\t");
	num_seq = strtok(NULL, "\t");
	sequon_list = strtok(NULL, "\n");
    
	if(ipi && description && prot_len && num_seq && sequon_list)
	{
		
		n_glycos_input gly;

		gly.ipi = strdup(ipi);
		gly.desc = strdup(description);
		sscanf(prot_len, "%d", &gly.prot_len);
		sscanf(num_seq, "%d", &gly.num_sequons);
		gly.sequon_list = strdup(sequon_list);
	
		n_glycos_storage.push_back(gly);

		return true;
	}

	return false;
}


void usage(char *argv_1)
{
	printf("Usage:\n%s n_glycos_output.txt trans_loop.txt organism_type(human = 1,mouse = 0) > outputfile.txt\n", argv_1);
	exit(-1);
}



int main(int argc, char **argv)
{

	if(argc != 4)
		usage(argv[0]);

    //get the necessary filenames
	string n_glycos_output, trans_loop_output;
	
	n_glycos_output = argv[1];
	trans_loop_output = argv[2];
	
	//convert filenames to C strings which can be passed into ifstream
	const char *n_glycos_ptr, *trans_loop_ptr;

	n_glycos_ptr = n_glycos_output.c_str();
	trans_loop_ptr = trans_loop_output.c_str();

	ifstream n_glycos_file(n_glycos_ptr);
	struct stat n_glycos_file_status;
	stat(n_glycos_ptr, &n_glycos_file_status);
	
	ifstream trans_loop_file(trans_loop_ptr);
	struct stat trans_loop_file_status;
	stat(trans_loop_ptr, &trans_loop_file_status);
	
	char line[MAXLINE_LEN];
	int count = 0;

	if(n_glycos_file.is_open())
	{
		n_glycos_file.getline(line, MAXLINE_LEN);
		count++;

		if(strlen(line) >= MAXLINE_LEN)
			{
				printf("ERROR, MAXIMUM LENGTH OF LINE EXCEEDED FOR LINE %d OF %s\n", count, argv[1]);
				exit(-1);
			}

		while(n_glycos_file.good())
		{
			n_glycos_file.getline(line, MAXLINE_LEN);
			count++;

			if(strlen(line) >= MAXLINE_LEN)
			{
				printf("ERROR, MAXIMUM LENGTH OF LINE EXCEEDED FOR LINE %d OF %s\n", count, argv[1]);
				exit(-1);
			}
				

			if(line == NULL)
				break;

			if(strlen(line) < 10)
				break;


			while(strlen(line) > 0 && line[strlen(line) - 1] == '\r')
			{
				line[strlen(line) - 1] = 0;
			}
				process_n_glycos_output(line);
			
		}

	}
	else
	{
		printf("\nCouldn't Open n_glycos output file\n");
	}

	count = 0;

	if(trans_loop_file.is_open())
	{
		trans_loop_file.getline(line, MAXLINE_LEN);
		count++;

		if(strlen(line) >= MAXLINE_LEN)
			{
				printf("ERROR, MAXIMUM LENGTH OF LINE EXCEEDED FOR LINE %d OF %s\n", count, argv[2]);
				exit(-1);
			}

		
		while(trans_loop_file.good())
		{
			trans_loop_file.getline(line, MAXLINE_LEN);
			count++;

			/*	if(strlen(line) >= MAXLINE_LEN)
			{
				printf("ERROR, MAXIMUM LENGTH OF LINE EXCEEDED FOR LINE %d OF\n", count, argv[2]);
				exit(-1);
			}*/

			if(strlen(line) < 10)
			break;

			while(strlen(line) > 0 && line[strlen(line) - 1] == '\r')
			{
				line[strlen(line) - 1] = 0;
			}

			process_trans_loop_line(line,argv[3]);
            
		}


	}
	else
	{
		printf("\nCouldn't Open trans_loop output file\n");
	}
	
	find_common_proteins();
	add_final_loop_info();

      	print_program_output();


	return 0;
}
