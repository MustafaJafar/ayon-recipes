// AYON CPP API Test
#include <iostream>
#include "AyonCppApi.h"

int main (){
    std::string project_name = "" ;
    std::cout << "Enter a project: ";
    std::cin >> project_name;

    AyonApi con = AyonApi(
        "log/log.json",           // extension will be always changed to json
        "your_access_token",      // This is a Bearer access token not AYON_API_KEY
        "https://your.server",    // with No trailing or forward slash at the end.
        project_name,
        "your-site-id"            // Your site id e.g. military-mouse-of-jest
    );
    
    std::string uri = "" ;
    std::cout << "Enter a uri to resolve: ";
    std::cin >> uri;

    std::pair<std::string, std::string> resolvedAsset = con.resolvePath(uri);
    std::cout << "The resolved path: " << resolvedAsset.second << std::endl;
    return 0;
}