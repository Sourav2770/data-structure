#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
};

struct node *root = NULL;

// Function prototypes
int display();
void insertion();
void deletion();

struct node *insert(struct node *root, struct node *newnode);
struct node *deleteNode(struct node *root, int value);
struct node *find_min(struct node *root);

// Traversal functions
void preOrder(struct node *root);
void inOrder(struct node *root);
void postOrder(struct node *root);

int main(void) {
    while (1) {
        int choice;
        printf("\n==== Binary Search Tree Menu ====\n");
        printf("0 -> Display Tree\n");
        printf("1 -> Insert Node\n");
        printf("2 -> Delete Node\n");
        printf("5 -> Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 0: display(); break;
            case 1: insertion(); break;
            case 2: deletion(); break;
            case 5: 
                printf("Exiting program...\n");
                return 0;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
    return 0;
}

// Insert a node into the tree and return the root
struct node *insert(struct node *root, struct node *newnode) {
    if (root == NULL)
        return newnode;
    if (newnode->data < root->data)
        root->left = insert(root->left, newnode);
    else
        root->right = insert(root->right, newnode);
    return root;
}

void insertion() {
    struct node *newnode = (struct node *)malloc(sizeof(struct node));
    if (newnode == NULL) {
        printf("Memory allocation failed!\n");
        return;
    }

    printf("Enter element to insert: ");
    scanf("%d", &newnode->data);
    newnode->left = newnode->right = NULL;

    root = insert(root, newnode);
    printf("Node inserted successfully!\n");
    display();
}

// Find the smallest node (used during deletion)
struct node *find_min(struct node *root) {
    while (root && root->left != NULL)
        root = root->left;
    return root;
}

// Delete a node from the tree and return the root
struct node *deleteNode(struct node *root, int value) {
    if (root == NULL) {
        printf("Value %d not found in the tree!\n", value);
        return root;
    }

    if (value < root->data)
        root->left = deleteNode(root->left, value);
    else if (value > root->data)
        root->right = deleteNode(root->right, value);
    else {
        // Found the node to delete
        if (root->left == NULL) {
            struct node *temp = root->right;
            free(root);
            return temp;
        } else if (root->right == NULL) {
            struct node *temp = root->left;
            free(root);
            return temp;
        }

        // Node with two children
        struct node *temp = find_min(root->right);
        root->data = temp->data;
        root->right = deleteNode(root->right, temp->data);
    }
    return root;
}

void deletion() {
    int value;
    printf("Enter the node value to delete: ");
    scanf("%d", &value);
    root = deleteNode(root, value);
    display();
}

// Traversals
void preOrder(struct node *root) {
    if (root == NULL)
        return;
    printf("%d ", root->data);
    preOrder(root->left);
    preOrder(root->right);
}

void inOrder(struct node *root) {
    if (root == NULL)
        return;
    inOrder(root->left);
    printf("%d ", root->data);
    inOrder(root->right);
}

void postOrder(struct node *root) {
    if (root == NULL)
        return;
    postOrder(root->left);
    postOrder(root->right);
    printf("%d ", root->data);
}

// Display all traversals
int display() {
    if (root == NULL) {
        printf("\nTree is empty!\n");
        return 1;
    }

    printf("\nCurrent Tree Traversals:\n");
    printf("Preorder: ");
    preOrder(root);
    printf("\nInorder:  ");
    inOrder(root);
    printf("\nPostorder:");
    postOrder(root);
    printf("\n");
    return 0;
}
