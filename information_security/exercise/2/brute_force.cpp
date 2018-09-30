#include <iostream>
#include <openssl/sha.h>
#include <string>
#include <fstream>
#include <chrono>
#include <thread>
#include <algorithm>
#include <iomanip>

std::string users[27][3] = {
        {"isla","78080165c82f6ee7","e667e7dd5adcaf77851e21349cf2a3b1"},
        {"daisy","3b647bf5ff1449b6","93c1bc8de3ec3815f60b55b8d490fd99"},
        {"anastasia","95ce618b1bc41202","c61846722948692d1b9728c728b7f8fd"},
        {"blanca","6c45126acfb7245a","0eb2c789085be36397177b040eace0c4"},
        {"aleksandra","4c5ef1d4c667081e","aca24364d1c5cbf0327799d0bf0da981"},
        {"bunny","a0bde8d99626fb69","9c87f70ead58e746ddd33d161f61aea2"},
        {"ana","118576545a3d488e","47777b0616ffc5004b1a9e8c618078ff"},
        {"dallas","41cf43998c3c65e7","7e3b87c4d772f2c4af0aceb227837ff5"},
        {"robo","3b647bf5ff1449b6","a1c2007e390138f8a485b4fd4ab31122"},
        {"hana","87c67bb4980bf974","ccdec81fa2cb8d868849520f7b29884c"},
        {"jack","0cf11b80ec60a51e","0e6eedaa577c492b6e7645c97710de51"},
        {"ema","7b9323bd87619f4b","b6117be544462c65b9c0e65c2b4c7c6c"},
        {"mihail","9dc4a06d24159048","2909c832abe4bec13704815c10515596"},
        {"maria","30b89b25d6a450fa","43bdc824b4e32817e9e8f82a977028ec"},
        {"emily","20526321dd6221a2","73d4dadd7320e56a96d1f496b6598db3"},
        {"jessica","0a78fb30f8bae58d","eaeca67e1f25592963a85e85e056c679"},
        {"jadyn","4302ff2f3b635fef","739937f37fdc3e977c5d869f07f65ec2"},
        {"david","a4bb02a136165271","a0b5ad10e20376a2d74b453641a0078b"},
        {"erin","cba1c18886dfec9b","7ede4b20550d214efcc7d41a98a7a5a6"},
        {"sara","6d8592aa055cf773","e9ee8cb4b5158c707c02cf7cef866ca2"},
        {"scout","6dc6ce247400629c","fe33e71abd3d737c523ffb72009139df"},
        {"sidney","9f585b860d7121ec","9f5127f360583296da80075cd821d32a"},
        {"student","3b647bf5ff1449b6","a1a1baa39bc08c809a930ca9fa6c1788"},
        {"tim","8af281a6503b79cb","c2b180b000705478e0eb30857f1feab2"},
        {"valentina","7913da612625b1a3","6eef82fc45e2f2a1a4e45d5a0000a169"},
        {"veeti","9e4607c2c0a63705","34447cc74793fa4a463f134f02b09d15"},
        {"winter","2fafb00afac6fa30","b28bfbc20da092ba2d37f45388badc70"}
    };

void check_password(const char *filename) {
    std::cout << "--- FILENAME: " << filename << " ---\n";
    std::string first_part = "potplantspw";
    unsigned char hash[SHA256_DIGEST_LENGTH];
    std::string line;
    std::ofstream outfile;

    outfile.open("crack_result.txt", std::ios::app);
    outfile << filename << std::endl;

    for (int i = 0; i < 27; i++) {
        std::ifstream the_file(filename);
        
        // first: add char at the beginning
        while(!the_file.eof()) {
            getline(the_file,line);    
            for (int z = 32; z <= 126; z++) {
                                
                std::string inpout_string = first_part + line + users[i][1];
                SHA256((const unsigned char *)inpout_string.c_str(), inpout_string.length(), hash);

                std::stringstream ss;
                for(int n = 0; n < 32; n++)
                {
                    ss << std::hex << std::setw(2) << std::setfill('0') << (int)hash[n];
                }
                std::string p = ss.str();
                p.resize(32);
                if (p == users[i][2]) {
                    std::string res = "username: " +  users[i][0] + "; password: " + line; 
                    outfile << res << std::endl; 
                    std::cout << res << std::endl;
                }
           }
        }

        the_file.close();
    }
}

int main() {
    check_password("/usr/share/dict/words");
    //check_password("brute/dict/words");
    
    return 0;
}