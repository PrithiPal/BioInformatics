

#include <iostream>
#include <fstream>
#include <sstream>
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
string n_glycos_file, trans_loop_file;
int first_domain_length=0, last_domain_length=0;
int first_domain_in=0;
int first_domain_out=0;
int last_domain_in=0;
int last_domain_out=0;
int first_glyco_domain_in=0;
int first_glyco_domain_out=0;
int last_glyco_domain_in=0;
int last_glyco_domain_out=0;

char location_of_first_domain='x';
char location_of_last_domain='x';

//store the input information
struct input_info
{
	char *ipi;
	char *desc;
	int prot_len;
	int num_sequons;
	char *seq_list;
	char *loop_info;
	char *loop_len_info;
};

//store a single segment for the loop length info
struct loop_len_segment
{
	char *loop;
	char location;
	int start;
	int finish;
	int len;
	int num_sequons_within;
};

//store a single segment for the glycosylation info
struct n_gly_segment
{
	char a, b, c, location;
	int position;
};

//store all input information
vector<input_info> input_info_storage;

//determine whether a sequon is inside, outside, or within a membrane
char find_location(int sequon_location, vector<loop_len_segment> loops)
{
	for(int i = 0; i < loops.size(); i++)
	{
		if(sequon_location >= loops.at(i).start && sequon_location <= loops.at(i).finish)
		{
			if(loops.at(i).location=='i'||loops.at(i).location=='o')
				return loops.at(i).location;
		}
	}

	return 'm';
}

//find number of sequons within the location bounded by start and finish
int find_num_sequons_within(int start, int finish, vector<n_gly_segment> n_gly)
{
	int count = 0;

	for(int i = 0; i < n_gly.size(); i++)
	{
		if(n_gly.at(i).position >= start && n_gly.at(i).position <= finish)
			count++;
	}

	return count;
}

//find average length of loops inside membrane
float find_average_inside_loop(vector<loop_len_segment> loops)
{
	float total = 0;
	int count = 0;

	for(int i = 0; i < loops.size(); i++)
	{
		if(loops.at(i).location == 'i')
		{
			count++;
			total += loops.at(i).len;
		}
	}

	if(count != 0)
		return total/count;
	else
		return total;
}

//find average length of loops outside membrane
float find_average_outside_loop(vector<loop_len_segment> loops)
{
	float total = 0;
	int count = 0;

	for(int i = 0; i < loops.size(); i++)
	{
		if(loops.at(i).location == 'o')
		{
			total += loops.at(i).len;
			count++;
		}
	}

	if(count != 0)
		return total/count;
	else
		return total;
}

//find average length of loops outside membrane with NxS/T sequons
float find_avg_outside_with_sequons(vector<loop_len_segment> loops)
{
	float total = 0;
	int count = 0;

	for(int i = 0; i < loops.size(); i++)
	{
		if(loops.at(i).location == 'o' && loops.at(i).num_sequons_within > 0)
		{
			count++;
			total += loops.at(i).len;
		}

	}

	//can't divide by zero, so do this check
	if(count != 0)
		return total/count;
	else
		return total;
}

//find average loop length inside cell with NxS/T sequons
float find_avg_inside_with_sequons(vector<loop_len_segment> loops)
{
	float total = 0;
	int count = 0;

	for(int i = 0; i < loops.size(); i++)
	{
		if(loops.at(i).location == 'i' && loops.at(i).num_sequons_within > 0)
		{
			count++;
			total += loops.at(i).len;
		}
	}

	//can't divide by zero so do this check
	if(count != 0)
		return total/count;
	else 
		return total;
}

string convert_to_string(int x)
{
 char buffer[20];

 sprintf(buffer, "%d", x);

 return string(buffer);
}

string calculate_first_domain(char * pch)
{
  string first_domain;
  char position;
  int start=0,end=0,length=0;
  sscanf(pch, "%c(%d-%d=%d),", &position, &start, &end, &length);
  
 stringstream ss;
 string s,s1,s2,s3;

 first_domain_length=length; //declared at very top
 location_of_first_domain=position;
 
 if (position=='o')
   first_domain_out=length;   //declared at top
 else if (position=='i')
   first_domain_in=length;
 else
   first_domain_out=-1;
 
 ss << position;
 ss >> s;

 s1= convert_to_string(start);

 s2= convert_to_string(end);
 
 s3= convert_to_string(length);
 
 //first_domain=s+"("+ to_string(start)+"-"+to_string(end)+"="+to_string(length)+")";
 first_domain=s+"("+s1+"-"+s2+"="+s3+")";
 return first_domain;
}

string calculate_last_domain(char * pch)
{
  string last_domain;
  char position;
  int start=0,end=0,length=0;
  sscanf(pch, "%c(%d-%d=%d),", &position, &start, &end, &length);
  
 stringstream ss;
 string s,s1,s2,s3;

 last_domain_length=length; //declared at very top

 location_of_last_domain=position;
 
 if (position=='o')
   last_domain_out=length;   //declared at top
 else if (position=='i')
   last_domain_in=length;
 else
   last_domain_out=-1;
 
 ss << position;
 ss >> s;

 s1= convert_to_string(start);

 s2= convert_to_string(end);
 
 s3= convert_to_string(length);
 
 // last_domain=s+"("+ to_string(start)+"-"+to_string(end)+"="+to_string(length)+")";
 last_domain=s+"("+s1+"-"+s2+"="+s3+")";
 
 return last_domain;
}

//function to calculate the first domain containing Glyco

int calculate_first_domain_glyco(int first_domain_length,int position_of_sequon,char location_of_first_domain)
{int length=0;

  if (position_of_sequon >= '0' && position_of_sequon <=first_domain_length)
     length=first_domain_length;

  if (location_of_first_domain =='i')
    first_glyco_domain_in=length;
  else if(location_of_first_domain =='o')
    first_glyco_domain_out=length;
  else 
    {first_glyco_domain_out=-1;
      last_glyco_domain_out=-1;}
  
  return length;}  

int calculate_last_domain_glyco(int last_domain_length,int protein_length,int position_of_sequon,char location_of_last_domain)
{int length=0;
  int start=0;
  start=protein_length-last_domain_length;

  if (position_of_sequon>=start)
     length=last_domain_length;
   
  if (location_of_last_domain =='i')
    last_glyco_domain_in=length;
  else if(location_of_last_domain=='o')
    last_glyco_domain_out=length;
  else 
    { last_glyco_domain_out=-1;
      last_glyco_domain_out=-1;}
  return length;
}

//free memory of loop length segment structure (pointer needs to be freed)
void free_loop_len_segment(vector<loop_len_segment> loop)
{
	for(int i = 0; i < loop.size(); i++)
	{
		free(loop.at(i).loop);
	}
}

//reads in all the input data, stores it and processes the necessary values
void process_output()
{
	//open an output file stream
	ofstream n_glycos_output_file, trans_loop_output_file;

	n_glycos_file=n_glycos_file+".txt";
	trans_loop_file=trans_loop_file+".txt";
	
	//open the files we want to write to
	n_glycos_output_file.open(n_glycos_file.c_str());
	trans_loop_output_file.open(trans_loop_file.c_str());
	
	n_glycos_output_file << "ID\tDescription\tProtein Length\tTMHMM Topology\tLoop Length Info\tList of Sequons and Locations" << endl;
	trans_loop_output_file << "ID\tDescription\tProtein Length\tTMHMM Topology\tSequon Positions\tList of Transmembrane Loops and Sequon Data\tAvg-loop.i\tAvg-loop.o\tAvg-loop (glyco).i\tAvg-loop (glyco).o\tFirstDomain\tLastDomain\tFirstDomain.Length\tFirstDomain.Out\tFirstDomain.In\tLastDomain.Length\tLastDomain.Out\tLastDomain.In\tFirstDomain.Glyco.Length\tFirstGlyco.Length.Out\tFirstGlyco.Legnth.In\tLastDomain.Glyco.Length\tLastGlyco.Length.Out\tLastGlyco.Length.In" << endl;

	for(int i = 1; i < input_info_storage.size(); i++)
	{

 first_domain_in=0;
 first_domain_out=0;
 last_domain_in=0;
 last_domain_out=0;
 first_glyco_domain_in=0;
 first_glyco_domain_out=0;
 last_glyco_domain_in=0;
 last_glyco_domain_out=0;
 
		//store the data from each line dynamically
		vector<n_gly_segment> sequons;
		vector<loop_len_segment> loops;
		string FirstDomain,LastDomain;

		//get the sequon information
		char *sequon_list = strdup(input_info_storage.at(i).seq_list);
		char *loop_information = strdup(input_info_storage.at(i).loop_info);
		char *loop_length_information = strdup(input_info_storage.at(i).loop_len_info);
		//printf("%s\n", loop_information);

		char *pch = strtok(input_info_storage.at(i).seq_list, " ");
        		
		while(pch != NULL)
		  {
		    n_gly_segment gly;
			sscanf(pch, "%c%c%c(%d)", &gly.a, &gly.b, &gly.c, &gly.position);
			//cout<<gly.position<<endl;
			sequons.push_back(gly);
			pch = strtok(NULL, " ");
		}

		//get the loop length information
		pch = strtok(input_info_storage.at(i).loop_len_info, " ");

		string first_domain=calculate_first_domain(pch);

		char*lastpch=pch;
		while(pch != NULL)
		{
			loop_len_segment loop_seg;
			loop_seg.loop = strdup(pch);
			sscanf(pch, "%c(%d-%d=%d),", &loop_seg.location, &loop_seg.start, &loop_seg.finish, &loop_seg.len);
			loops.push_back(loop_seg);
			lastpch=pch;
			pch = strtok(NULL, " ");
		}

		string last_domain=calculate_last_domain(lastpch);
		
		//find whether each sequon is inside, outside, or within the membrane
		for(int a = 0; a < sequons.size(); a++)
		{
			sequons.at(a).location = find_location(sequons.at(a).position, loops);
		}

		//find the number of sequons present in each loop
		for(int b = 0; b < loops.size(); b++)
		{
			loops.at(b).num_sequons_within = find_num_sequons_within(loops.at(b).start, loops.at(b).finish, sequons);
		}

		//find the position of first and last sequon
		int last=sequons.size();
		//cout<<sequons.at(0).position<<"----last---"<<sequons.at(last-1).position<<endl;

		//function to see if the first domain has any Glyco site
		int first_domain_glyco_length=calculate_first_domain_glyco(first_domain_length,sequons.at(0).position,location_of_first_domain);
		//	cout<<first_domain_glyco_length<<endl;

     
		//function to see if the last domain has any Glyco
		int last_domain_glyco_length=calculate_last_domain_glyco(last_domain_length,input_info_storage.at(i).prot_len,sequons.at(last-1).position,location_of_last_domain);
		//cout<<last_domain_glyco_length<<endl;
		
		//string to store the data and append further data to
		string data;
		char *data_segment;

		//store the n_glycos output data
		for(int c = 0; c < sequons.size(); c++)
		{
			asprintf(&data_segment, "%c%c%c(%d)/%c ", sequons.at(c).a, sequons.at(c).b, sequons.at(c).c, sequons.at(c).position, sequons.at(c).location);
			data.append(data_segment, strlen(data_segment));
			data_segment = NULL;
		}

		
		//write output to file
		n_glycos_output_file << input_info_storage.at(i).ipi << "\t" << input_info_storage.at(i).desc << "\t"<< input_info_storage.at(i).prot_len << "\t" << loop_information
			<< "\t" << loop_length_information << "\t" << data << endl;
	  
		data.clear();

		//store the trans_loop output data
		for(int d = 0; d < loops.size(); d++)
		{
			asprintf(&data_segment, "%c(%d-%d=%d)/%d ", loops.at(d).location, loops.at(d).start, loops.at(d).finish, loops.at(d).len, loops.at(d).num_sequons_within);
			data.append(data_segment, strlen(data_segment));
			data_segment = NULL;
		}

		//write output to file
		trans_loop_output_file << input_info_storage.at(i).ipi << "\t" <<input_info_storage.at(i).desc<<"\t" << input_info_storage.at(i).prot_len 
			<< "\t" <<input_info_storage.at(i).loop_info << "\t" << sequon_list << "\t" << data << "\t" << find_average_inside_loop(loops) 
				       << "\t" << find_average_outside_loop(loops) << "\t" << find_avg_inside_with_sequons(loops) << "\t" << find_avg_outside_with_sequons(loops)<< "\t" <<first_domain <<"\t"<<last_domain<<"\t"<<first_domain_length<<"\t"<<first_domain_out<<"\t"<<first_domain_in<<"\t"<<last_domain_length<<"\t"<<last_domain_out<<"\t"<<last_domain_in<<"\t"<<first_domain_glyco_length <<"\t"<<first_glyco_domain_out<<"\t"<<first_glyco_domain_in<<"\t"<<last_domain_glyco_length<<"\t"<<last_glyco_domain_out<<"\t"<<last_glyco_domain_in<<endl;

		
		data.clear();

		//free data for the next iteration
		free_loop_len_segment(loops);
		free(sequon_list);
		free(loop_length_information);
		free(loop_information);
		loops.clear();
	    sequons.clear();
	}

	//close files, we are done
	n_glycos_output_file.close();
	trans_loop_output_file.close();
}


//how to use the program
void usage(char *argv_1)
{
	printf("Usage:\n%s common_input.txt\n", argv_1);
	exit(-1);
}

//each line of input needs to be processed
void process_line(char *line)
{
	//check if null
	if(!line)
		return;

	//declare pointers to store all necessary fields
	char *ipi,  *prot_len, *num_sequons, *seq_list, *loop_info, *loop_len_info;
	char *desc;
	
    //tokenize input
   
	ipi = strtok(line, "\t");
       	desc = strtok(NULL, "\t");
	prot_len = strtok(NULL, "\t");
	num_sequons = strtok(NULL, "\t");
	seq_list = strtok(NULL, "\t");
	loop_info = strtok(NULL, "\t");
	loop_len_info = strtok(NULL, "\n");

	input_info info;
	
	//check if null and if not copy input into structure for further analysis
	if(ipi)
		info.ipi = strdup(ipi);
       	if(desc)
       		info.desc = strdup(desc);
	if(prot_len)
		sscanf(prot_len, "%d", &info.prot_len);
	if(num_sequons)
		sscanf(num_sequons, "%d", &info.num_sequons);
	if(seq_list)
		info.seq_list = strdup(seq_list);
	if(loop_info)
		info.loop_info = strdup(loop_info);
	if(loop_len_info)
		info.loop_len_info = strdup(loop_len_info);

	input_info_storage.push_back(info);
}


int main()
{
  char command[100];

  string filename1,filename2,org_type;
  cout<<"Enter the name of n_glyco file(without .txt)"<<endl;
  cin>>filename1;
  cout<<"Enter the name of transloop file(without .txt)"<<endl;
  cin>>filename2;
  cout << "Enter the type of organism(1 = sp,0 = IPI) " << endl;
  cin >> org_type;
    
  //compile the file
  
  strcpy(command,"g++ -o commonfile common.cpp");
  system(command);
  
  string objectname="./commonfile"; //fixed in above line
  
  string inter_command= objectname+" "+filename1+".txt"+" "+filename2+".txt"+" "+ org_type + " >common_output.txt";
 
  strcpy(command,inter_command.c_str());
  // strcpy(command,"./commonfile n_glyco.txt output.txt >common_input.txt");
  system(command);

   cout<<"common_output.txt has been created"<<endl;
  
    //get the necessary filenames
	string common_output;

	printf("Please Enter a Transmembrane Loop Information Filename\n");
	cin>>trans_loop_file;

	printf("Please Enter a N_Glycosylation Information Filename\n");
	cin>>n_glycos_file;


	common_output = "common_output.txt";
	const char *common_ptr = common_output.c_str();

	common_ptr = common_output.c_str();
	
	ifstream common_file(common_ptr);
	struct stat common_file_status;
	stat(common_ptr, &common_file_status);

	char line[MAXLINE_LEN];
	char column[MAXLINE_LEN];
	
	if(common_file.is_open())
	{
		// common_file.getline(line, MAXLINE_LEN);

		while(common_file.good())
		{
			common_file.getline(line, MAXLINE_LEN);

			if(line == NULL || strlen(line) < 10)
				break;

			while(strlen(line) > 0 && line[strlen(line) - 1] == '\r')
			{
				line[strlen(line) - 1] = 0;
			}	

					process_line(line);
		}
	}
	else
	{
		printf("\nCouldn't Open common_output_file\n");
	}
	process_output();

	return 0;
}
