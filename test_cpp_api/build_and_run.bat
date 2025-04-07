rmdir /s /q build
cmake -S . -B build -DJTRACE=0 
devenv build/main.sln /Build
build\Debug\main.exe