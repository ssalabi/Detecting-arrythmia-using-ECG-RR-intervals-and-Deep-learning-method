# dl_project

Project structure:

*  /src/
    * neural_network/* : modeling, dataloader and training
    * preprocessing/*  : data downloading, preproccessing and exploration
    * cs236781/*       : utilities from the course
    * train.ipynb      : training notebook
    * check_af*        : some of the models mentioned in the report
    * data/            : folder that will contain data after the preproccessing 
    
    
How to reproduce results:

*  Running the preprocessing/pre_process.ipynb downloads and creates the data
*  Running the train.ipynb with the relevant data path(according to the use case you want)
   to train and see results.