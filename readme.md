# Final degree project: Algorithm executer backend server.

In this version we are going to use fastapi in order to improve the backend performance, also, if in the future someone wants to make the extraction of the data from other place that is not a frontend, that person would have to modify the controller and add a method to the repository.

## Let's do some research about fastapi.

In order to take advantage of all the features os this framework i will make some research before start the project, i am goint to use vertical slicing + hexagonal arquitecture but without the aplication layer, services would be in the domain.

### Annotations, map DTO and error handlers

The first thing that I would like to ensure are the different tools to make the infrastructure layer more efficient, so we have to make some research about how stablish a controller:

```python

```

Once we have the controllers in a different file, we would add the DTO to map the body automatically:

* Structure of the body at the run endpoint:

```json

```

Following the python fastAPI doc we can create this DTO with the following code:

```python

```

Now the idea is to handle the errors directly with the tools that FastAPI gives because is really abstract to desacoplate this logic and i dont think that is worth

raise HTTP..