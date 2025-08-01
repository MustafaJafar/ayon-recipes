# My Full Steps to be able to use AYON CPP API 

## About AYON CPP API
It's a static library that includes a subset of AYON API functions. It was primarily developed to support the development of [ayon-usd-resolver](https://github.com/ynput/ayon-usd-resolver).

> It's called static because once the static library is linked into your executable at build time, the code from that library becomes part of your binary. After that, you no longer need the `.lib` or `.a` file to run your program.

## Fetch the AYON CPP Lib

```
git clone https://github.com/ynput/ayon-cpp-api.git
cd ayon-cpp-api
git submodule update --init --recursive
```

## Create a cpp example and its cmake file

On my side I made this simple project structure:
```
.
├─ ext/ayon-cpp-api
├─ CMakelists.txt
└─ main.cpp
```
> Note: You need to use at least C++17 in CMake

> [!IMPORTANT]
> The auth key used in the cpp example is an [Authentication Token](https://community.ynput.io/t/ayon-rest-api-guide/1268#get-authentication-token-6) which is not an `AYON_API_KEY`.
> Also, don't add a trailing forward slash to your AYON server URL.


## Build And Run Commands

- **Build CPP**
    ```
    git submodule update --init --recursive
    cd ext\ayon-cpp-api
    python AyonBuild.py --setup
    python AyonBuild.py --runStageGRP CleanBuild
    ```

- **Build CPP Example**
    ```
    rmdir /s /q build
    cmake -S . -B build -DJTRACE=0 
    cmake --build ./build --config Debug -j12
    ```
- **Run CPP Example**
    ```
    build\Debug\main.exe
    ```

**Expected Output**:
```
Enter a project: Animal_Logic_ALab
Enter a uri to resolve: ayon+entity://Animal_Logic_ALab/assets/book_encyclopedia01?product=usdAsset&version=v002&representation=usd
The resolved path: H:\AYON\projects\Animal_Logic_ALab\assets\book_encyclopedia01\publish\usd\usdAsset\v002\ALA_book_encyclopedia01_usdAsset_v002.usd
```