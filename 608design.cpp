#include <iostream>
#include <map>
using namespace std;

import csv;     // not need install, just use

(1) Read .csv "airport"
map<string, string> AirportID;    //mapping AirportID and Airport
/* AirportID   Airport
   13215        JFK
   19893        LA
   .......
*/
for row in reader  //read .csv file(python style)
    AirportID[row['AirportID']] = row['Airport']


(2) define class TwoNodeInfo{
private:
    string Node1, Node2;
    int distance, delay;
public:
    TwoNodeInfo(string Node1, string Node2, int distance, int delay)
    :Node1(Node1), Node2(Node2), distance(distance), delay(delay) {}
};

read .csv "delay"
/* origin   destination   distance   delay
   15635    16548         700        10
   48949    15968         800        20
   ..........
*/
TwoNodeInfo info[];
int num=0;
for row in reader  //read .csv file(python style)
   info[i].Node1 = row['orgin'];
   info[i].Node2 = row['destination'];
   info[i].distance = row['distance'];
   info[i].delay = row['delay'];
   // I don't know 这里是否存在string和int不匹配的问题
   num++;
/* till now, we've got all information*/

(3)
int main() {
/*get all nodes*/
    string node[];
    int j=0;
    for(map<string, string>::iterator i = AirportID.begin(); i!= AirportID.end();i++){
        node[j] = i->first;
        j++;
    }
    //不想用map，就把csv文件再读一遍

/*produce node_list*/
    noed_list;  //我没看懂node_list那个函数
    for(int i=0; i<num; i++){
       把 (info[i].Node1, info[i].Node2, info[i].distance) 加入node_list
    }

/* 输入起始点后，得到dijstrapath. (node[i],distanceI)---(node[i+1],distanceI+1)
 * 我们得到所有shortest path上的所有nodes，带回info可以搜索到最小的delay
 * */

}