// AYON CPP API Test
#include <iostream>
#include "dotenv.h"
#include "AyonCppApi.h"

int main (){

    dotenv::init(); // loads from ".env"

    std::string project_name = "" ;
    std::cout << "Enter a project: ";
    std::cin >> project_name;

    AyonApi con = AyonApi(
        std::getenv("LOG_FILE"),         // extension will be always changed to json.
        std::getenv("AYON_API_KEY"),     // This is can be a Bearer access token or AYON_API_KEY.
        std::getenv("AYON_SERVER_URL"),  // with No trailing or forward slash at the end.
        project_name,
        std::getenv("AYON_SITE_ID")      // Your site id e.g. military-mouse-of-jest
    );
    
    std::string uri = "" ;
    std::cout << "Enter a uri to resolve: ";
    std::cin >> uri;

    std::pair<std::string, std::string> resolvedAsset = con.resolvePath(uri);
    std::cout << "The resolved path: " << resolvedAsset.second << std::endl;
    return 0;
}