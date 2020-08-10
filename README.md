# Implementation of NEAT on NES based Game

**Author : Bhargav Parmar** </br>
**Co-Author : Sudeep Kuchara**

## Introduction of NEAT:

### Neuro-Evolution Augmenting Topologies: 
NeuroEvolution can optimize and evolve neural network structure, and the NEAT algorithm was one of the first to show it as a viable approach. 
Typically in Neural Network fixed structure of network is being used but what if it evolve through Genetic Algorithm? That's a really good idea.Now the problem is how do we will be 
encoding and representing individuals genetically in algorithm and how the algorithm will handle evolutionary process like selection, mutation and cross over. In biology, we have a 
genotype and a phenotype. A genotype is the genetic representation of a creature and the phenotype is the actualized physical representation of the creature. Evolutionary algorithms
always heavily mirror biology, neuroevolution being no different in this respect. In terms of encoding there is two category direct and indirect.A direct encoding will explicitly specify everything about an individual. If it represents a neural network this means that each gene will directly be linked to some node, connection, or property of the network. This can be a binary encoding of 1s and 0s, a graph encoding (linking various nodes by weighted connections), or something even more complex. The point is that there will always be a direct connection between genotype and phenotype that is very obvious and readable.

An indirect encoding is the exact opposite. Instead of directly specifying what a structure may look like, indirect encodings tends to specify rules or parameters of processes for creating an individual. As a result, indirect encodings are much more compact. The flip side is that setting the rules for an indirect encoding can result in a heavy bias within the search space, therefore, it is much harder to create an indirect encoding without substantial knowledge about how the encoding will be used.

The NEAT algorithm chooses a direct encoding methodology because of this. Their representation is a little more complex than a simple graph or binary encoding, however, it is still straightforward to understand. It simply has two lists of genes, a series of nodes and a series of connections. To see what this looks like visually: 

![alt text](https://miro.medium.com/max/875/0*Kze4g6cLA3maofxq.png)

Input and output nodes are not evolved in the node gene list. Hidden nodes can be added or removed. As for connection nodes, they specify where a connection comes into and out of, the weight of such connection, whether or not the connection is enabled, and an innovation number. 

### Mutation:
Mutation can either mutate existing connections or can add new structure to a network. If a new connection is added between a start and end node, it is randomly assigned a weight.If a new node is added, it is placed between two nodes that are already connected. The previous connection is disabled (though still present in the genome). The previous start node is linked to the new node with the weight of the old connection and the new node is linked to the previous end node with a weight of 1. This was found to help mitigate issues with new structural additions.

![alt text](http://miro.medium.com/max/558/0*hk8JqrWFbRiG04L2.jpg)

### Crossover:
when it comes time to crossover two individuals, this can be done with much less chance of creating individuals that are non-functional. Each gene can be aligned and (potentially) crossed-over. Each time a new node or new type of connection occurs, a historical marking is assigned, allowing easy alignment when it comes to breed two of our individuals.

![alt text](https://miro.medium.com/max/875/0*N4j_sl8M05G6pXZV.png)

Read full article here: https://towardsdatascience.com/neat-an-awesome-approach-to-neuroevolution-3eca5cc7930f

## Code Requirements

**pip install requirements.txt**

## Outcome of Implimentation:
For implementation purpose we decided to use NES based games(The Nintendo Entertainment System (NES) is an 8-bit third-generation home video game console produced, released, and marketed by Nintendo). The outcome of the implementation on game is below where agent fought with final boss and won.

![alt text](https://user-images.githubusercontent.com/62926512/89755223-499f1e80-dafc-11ea-950a-8436d3b7e203.png)

