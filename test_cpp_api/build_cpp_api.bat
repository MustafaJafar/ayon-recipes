cd ext\ayon-cpp-api
git submodule update --init --recursive
python AyonBuild.py --setup
python AyonBuild.py --runStageGRP CleanBuild

cd ../..