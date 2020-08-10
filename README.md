# Implementation of NEAT on NES based Game
## Neuro-Evolution Augmenting Topologies: 
NeuroEvolution can optimize and evolve neural network structure, and the NEAT algorithm was one of the first to show it as a viable approach. 
Typically in Neural Network fixed structure of network is being used but what if it evolve through Genetic Algorithm? That's a really good idea.Now the problem is how do we will be 
encoding and representing individuals genetically in algorithm and how the algorithm will handle evolutionary process like selection, mutation and cross over. In biology, we have a 
genotype and a phenotype. A genotype is the genetic representation of a creature and the phenotype is the actualized physical representation of the creature. Evolutionary algorithms
always heavily mirror biology, neuroevolution being no different in this respect. In terms of encoding there is two category direct and indirect.A direct encoding will explicitly specify everything about an individual. If it represents a neural network this means that each gene will directly be linked to some node, connection, or property of the network. This can be a binary encoding of 1s and 0s, a graph encoding (linking various nodes by weighted connections), or something even more complex. The point is that there will always be a direct connection between genotype and phenotype that is very obvious and readable.

An indirect encoding is the exact opposite. Instead of directly specifying what a structure may look like, indirect encodings tends to specify rules or parameters of processes for creating an individual. As a result, indirect encodings are much more compact. The flip side is that setting the rules for an indirect encoding can result in a heavy bias within the search space, therefore, it is much harder to create an indirect encoding without substantial knowledge about how the encoding will be used.

The NEAT algorithm chooses a direct encoding methodology because of this. Their representation is a little more complex than a simple graph or binary encoding, however, it is still straightforward to understand. It simply has two lists of genes, a series of nodes and a series of connections. To see what this looks like visually, I have a picture from the original paper here:
Image for post
Image for post

Input and output nodes are not evolved in the node gene list. Hidden nodes can be added or removed. As for connection nodes, they specify where a connection comes into and out of, the weight of such connection, whether or not the connection is enabled, and an innovation number 
