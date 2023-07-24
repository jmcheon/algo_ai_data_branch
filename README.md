
## Algo, AI, data branch

<table>
<tr><th>Title</th><th>Team</th><th>Time</th><th>XP</th><th>Description</th></tr>
<tr><td>[DEPRECATED]ml_module <td>Solo<td>5days<td>15000<td>This is Bootcamp Machine Learning created by the Paris-based student organization 42 AI.</tr>
<tr><td>[DEPRECATED]python_module <td>Solo<td>5days<td>6000<td>This is Bootcamp Python created by the Paris-based student organization 42 AI.</tr>
<tr><td>ft_linear_regression <td>Solo<td>49h<td>4200<td>In this project, you will implement your first machine learning algorithm.</tr>
<tr><td>dslr <td>Group 2<td>98h<td>6000<td>Write a classifier and save Hogwarts!</tr>
<tr><td>Leaffliction <td>Group 2-3<td>294h<td>15750<td>Image classification by disease recognition on leaves.</tr>
<tr>
	<td>Multilayer_Perceptron 
	<td>Solo
	<td>98h
	<td>9450
	<td>This project is an introduction to artificial neural networks, with the implementation of a multilayer perceptron.<br>
		<a href="https://www.google.com/search?q=artificial neural network" target="_blank">#artificial neural network</a>
		<a href="https://www.google.com/search?q=feedforward" target="_blank">#feedforward</a>
		<a href="https://www.google.com/search?q=backpropagation" target="_blank">#backpropagation</a>
		<a href="https://www.google.com/search?q=gradient descent" target="_blank">#gradient descent</a>
		<a href="https://www.google.com/search?q=softmax function" target="_blank">#softmax function</a>
		<a href="https://en.wikipedia.org/wiki/Cross_entropy#Cross-entropy_error_function_and_logistic_regression" target="_blank">#binary cross-entropy error function</a>
		<a href="https://en.wikipedia.org/wiki/Early_stopping" target="_blank">#early stopping</a>
</tr>
<tr>
	<td>Total_perspective_vortex</td>
	<td>Solo</td>
	<td>98h</td>
	<td>9450</td>
	<td>Brain computer interface with machine learning based on electroencephalographic data. <br>
		<a href="https://www.google.com/search?q=python MNE" target="_blank">#python MNE</a>
		<a href="https://www.google.com/search?q=EEG" target="_blank">#EEG</a>
		<a href="https://www.google.com/search?q=dimensionality reduction" target="_blank">#dimensionality reduction</a>
		<a href="https://www.google.com/search?q=scikit-learn pipeline" target="_blank">#scikit-learn pipeline</a>
	</td>
</tr><tr><td>lem-in <td>Group 2<td>98h<td>9450<td>This project is meant to make you code an ant farm manager.</tr>
<tr><td>n-puzzle <td>Group 2<td>98h<td>9450<td>The goal of this project is to programmatically solve the N-puzzle.</tr>
<tr><td>rubik <td>Group 2<td>98h<td>9450<td>This project will make you write a program that solves Rubik’s Cubes with minimum spins.</tr>
<tr><td>expert-system <td>Group 2<td>98h<td>9450<td>The goal of this project is to make a propositional calculus expert system.</tr>
<tr><td>krpsim <td>Group 2-3<td>49h<td>9450<td>This project may be an algorithmic project, an operational research project, an AI project as well as an industrial project... As you like.</tr>
<tr><td>Gomoku <td>Group 2<td>196h<td>25200<td>The goal of this project is to make an AI capable of beating human players at Gomoku.</tr>
</table>

```mermaid
pie  title XP for AI projects
	"Leaffliction"  : 15750
	"ft_linear_regression"  : 4200
	"dslr"  : 6000
	"Multilayer_Perceptron"  : 9450
	"Total_perspective_vortex"  : 9450
	"lem-in"  : 9450
	"n-puzzle"  : 9450
	"rubik"  : 9450
	"expert-system"  : 9450
	"krpsim"  : 9450
	"Gomoku"  : 25200
```

```mermaid
pie  title required hours for AI projects
	"Leaffliction"  : 294
	"ft_linear_regression"  : 49
	"dslr"  : 98
	"Multilayer_Perceptron"  : 98
	"Total_perspective_vortex"  : 98
	"lem-in"  : 98
	"n-puzzle"  : 98
	"rubik"  : 98
	"expert-system"  : 98
	"krpsim"  : 49
	"Gomoku"  : 196
```


### AI, data branch
```mermaid
flowchart LR
	a(python module)
	b(ml module)
	0(AI, data) --49h, 4200XP--> A((ft_linear_regression))
	B((dslr)):::group
	A((ft_linear_regression)) --98h, 6000XP --> B
	B -- 98h, 9450XP --> C((Multilayer Perceptron))
	B -- 98h, 9450XP --> D((Total perspective vortex))
	B -- 294h, 15750XP --> E((Leaffliction)):::group
    classDef group fill:#f96
```

### Algo branch
```mermaid
flowchart LR
	0(Algo) -- 98h, 9450XP --> A((lem-in)):::group
	0 -- 98h, 9450XP -->B((n-puzzle)):::group
	0 -- 98h, 9450XP -->C((rubik)):::group
	
	B -- 196h, 25200XP --> D((Gomoku)):::group
	B -- 98h, 9450XP --> E((expert-system)):::group
	B -- 49h, 9450XP --> F((krpsim)):::group

    classDef group fill:#f96
```
