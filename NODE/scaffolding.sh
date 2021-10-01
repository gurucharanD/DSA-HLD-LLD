read -p 'Enter Location to create scaffolding...(use / as delimiter)' DESTINATION_FOLDER
echo 'cloning folder structure from githib....'
git clone https://github.com/Srivasthava12/node-temp.git ./temp
echo 'cloning folder structure done....'
echo $DESTINATION_FOLDER
echo 'cloning to your specified folder....'
cd ./temp
# rm -R -f .git
cp -a . $DESTINATION_FOLDER
echo 'scaffolding created'
cd $DESTINATION_FOLDER
echo 'scaffolding created initializing git..'
git init
echo 'just a moment'
code .
