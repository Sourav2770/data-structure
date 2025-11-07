#include <stdio.h>
#include <stdlib.h>

#define MAX 100


struct Node {
    int vertex;
    struct Node* next;
};

struct Graph {
    int numVertices;
    struct Node** adjLists;
    int* visited;
};


struct Stack {
    int items[MAX];
    int top;
};

struct Node* createNode(int v) {
    struct Node* newNode = malloc(sizeof(struct Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}


struct Graph* createGraph(int vertices) {
    struct Graph* graph = malloc(sizeof(struct Graph));
    graph->numVertices = vertices;

    graph->adjLists = malloc(vertices * sizeof(struct Node*));
    graph->visited = malloc(vertices * sizeof(int));

    for (int i = 0; i < vertices; i++) {
        graph->adjLists[i] = NULL;
        graph->visited[i] = 0;
    }

    return graph;
}


void addEdge(struct Graph* graph, int src, int dest) {
    struct Node* newNode = createNode(dest);
    newNode->next = graph->adjLists[src];
    graph->adjLists[src] = newNode;
}


struct Stack* createStack() {
    struct Stack* stack = malloc(sizeof(struct Stack));
    stack->top = -1;
    return stack;
}

void push(struct Stack* stack, int value) {
    stack->items[++stack->top] = value;
}

int pop(struct Stack* stack) {
    if (stack->top == -1)
        return -1;
    return stack->items[stack->top--];
}


void topologicalSortUtil(struct Graph* graph, int vertex, struct Stack* stack) {
    graph->visited[vertex] = 1;

    struct Node* temp = graph->adjLists[vertex];
    while (temp) {
        int adjVertex = temp->vertex;
        if (!graph->visited[adjVertex]) {
            topologicalSortUtil(graph, adjVertex, stack);
        }
        temp = temp->next;
    }

    
    push(stack, vertex);
}


void topologicalSort(struct Graph* graph) {
    struct Stack* stack = createStack();

    for (int i = 0; i < graph->numVertices; i++) {
        if (graph->visited[i] == 0)
            topologicalSortUtil(graph, i, stack);
    }

    printf("Topological Sort Order:\n");
    while (stack->top != -1) {
        printf("%d ", pop(stack));
    }
    printf("\n");
}


int main() {
    struct Graph* graph = createGraph(6);

    
    addEdge(graph, 5, 2);
    addEdge(graph, 5, 0);
    addEdge(graph, 4, 0);
    addEdge(graph, 4, 1);
    addEdge(graph, 2, 3);
    addEdge(graph, 3, 1);

    
    topologicalSort(graph);

    return 0;
}
