#include <string>
#include <unordered_map>
class Solution
{
public:
    bool isAnagram(std::string s, std::string t)
    {
        if (s.length() != t.length())
        {
            return false;
        }

        std::unordered_map<char, int> s_map;
        std::unordered_map<char, int> t_map;

        for (char c : s)
        {
            if (s_map.count(c) > 0)
            {
                s_map[c]++;
            }
            else
            {
                s_map[c] = 1;
            }
        }

        for (char c : t)
        {
            if (s_map.count(c) > 0)
            {
                t_map[c]++;
            }
            else
            {
                t_map[c] = 1;
            }
        }

        return s_map == t_map;
    }
};
