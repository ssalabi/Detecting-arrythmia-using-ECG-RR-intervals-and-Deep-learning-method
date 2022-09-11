<h1>Detecting-arrythmia-using-ECG-RR-intervals-and-Deep-learning-method</h1>

<h2>Description</h2>
In this project, we aim to reproduce a model from a paper that was built to detect Atrial fibrillation (AF) from long ECG recordings and 
thus provide a robust diagnosis support system for AF. We implemented a classification Bidirectional Recurrent Neural Network (BRNN) that will get RR 
intervals as input and will predict if an atrial fibrillation is present or not. The data was preprocessed and 
split into overlapping 100 beats of RR intervals.
<br />

<h2>Article reproduced</h2>
 Faust et al. “Automated detection of atrial fibrillation using long short-term memory network with RR"
interval signals <br />

<h2>Project structure</h2>:
*  /src/ <br />
    * neural_network/* : modeling, dataloader and training <br />
    * preprocessing/*  : data downloading, preproccessing and exploration <br />
    * cs236781/*       : utilities from the course <br />
    * train.ipynb      : training notebook <br />
    * check_af*        : some of the models mentioned in the report <br />
    * data/            : folder that will contain data after the preproccessing <br />
    
<h2>How to reproduce results:</h2>

*  Running the preprocessing/pre_process.ipynb downloads and creates the data <br />
*  Running the train.ipynb with the relevant data path(according to the use case you want)
   to train and see results.

<h2>Dataset</h2>

- <b>MIT BIH Atrial Fibrillation from Physionet</b>

<h2>Language Used</h2>

- <b>Python</b> 

<h2>Packages Used </h2>

- <b>Pandas</b> 
- <b>Matplotlib</b>
- <b>Pytorch</b> 


