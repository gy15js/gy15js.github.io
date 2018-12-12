# AssessmentOne
This repository contains the final model created in the programming module practicals through semester one.


The model is a square grid, with 10 agents moving around it and eating the said environment to continue moving for as long as the model runs.

Click the 'run' button on the python window to get the model pop up window to appear, and then on the drop down menu click 'Run Model'.


The model presents agents moving around an environment and eating the environment as they move. This is through classes, functions and working with extra files and the web.  

The in.txt and agentframework.py are two files that need to be downloaded. Without these the model will not run so ensure these are in the same folder as the model .py file and open the agent framework.py file in the python console too.

No changes or additions need to be made to this model.


For the agents to move around the environment they need to eat to ensure the store is fulfilled to allow movement.

Additionally, there are two styles of movement:
-Normal: This is normal movement through the environment and does not take as much store to do so.
-Boost: This is a larger movement that is available to the agents when the store is over a certain amount, boost movement also takes more out of the store.

It should be noted that the agents do not continuously eat either. If the store is above 150, they won't eat when they move around the environment, until their store depletes enough.

The type of movement is displayed in the kernel while the model is running, as well as a 'not hungry!' message when the store is full.

This is a continuous model so it will only stop when the model window is closed.
