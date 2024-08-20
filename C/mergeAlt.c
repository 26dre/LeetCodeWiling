// #include <stdio.h>
// #include <string.h>
// #include <stdlib.h>

// #define SPACE ' '

// char * mergeAlternately(char * word1, char * word2){

//     u_int16_t word1_len = strlen(word1); 
//     u_int16_t word2_len = strlen(word2); 
//     u_int16_t len_to_dec = word1_len + word2_len;
//     printf("Len to dec = %d\n", len_to_dec);
//     char* ret_str = (char*) malloc(((len_to_dec) + 1) * sizeof(char));

//     ret_str[len_to_dec] = '\0';

//     u_int16_t left_ptr = 0; 
//     u_int16_t right_ptr = 0; 
//     u_int16_t ret_str_ptr = 0; 

//     for (int i = 0; i < len_to_dec; i += 1) {
//         if (left_ptr < word1_len) {
//             ret_str[ret_str_ptr] = word1[left_ptr]; 
//             ret_str_ptr += 1; 
//             left_ptr += 1; 
//         }

//         if (right_ptr < word2_len) {
//             ret_str[ret_str_ptr] = word2[right_ptr]; 
//             ret_str_ptr += 1; 
//             right_ptr += 1; 
//         }
//     }

//     return ret_str;

// }

// int main() {
//     printf("Hello world\n");
//     char* c = "abc"; 
//     char* other = "pqr";
//     char* res = mergeAlternately(c, other); 
//     printf("%s\n", res);

//     free(res);
//     // printf("c len = %lu", strlen(c));
// }

