// AYON CPP API Test
#include "AyonCppApi.h"

int main (){
    AyonApi con = AyonApi(
        "log/log.json",
        "your_access_token", // This is a Bearer access token not AYON_API_KEY
        "https://your.server", // with No trailing forward slash /
        "project_name",
        "testSiteId"
    );
    return 0;
}