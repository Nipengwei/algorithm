# -*- coding:utf-8 -*-
class Solution:
    def replaceSpace(self, s):
        return s.replace(" ", "%20")

'''
C code

void replaceSpace(char *str,int length) {
	if(str == NULL && length <= 0){return;}
    int spacenum=0,i;
    for(i=0; str[i] != '\0'; i++){
        if(str[i]==' ') spacenum++;
    }
    int newlen = i+spacenum*2;
    if(newlen > length){return;}
    while(i>=0 && newlen > i){
        if(str[i] == ' '){
            str[newlen--] = '0';
            str[newlen--] = '2';
            str[newlen--] = '%';
        }
        else{
            str[newlen--] = str[i];
        }
        --i;
    }
}
'''