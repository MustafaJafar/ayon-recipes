# My Full Steps to be able to use AYON CPP API 

## Fetch the AYON CPP Lib
It's a static library which means you can use it without building it?

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
```
rmdir /s /q build
cmake -S . -B build -DJTRACE=0 
devenv build/main.sln /Build 
build\Debug\main.exe
```
