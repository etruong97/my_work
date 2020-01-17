/*
C343 Summer 2019
Lab 18
Evan Truong
etruong
 */

import javax.swing.text.html.MinimalHTMLWriter;
import java.util.*;

public class AdjGraph implements Graph {
    private int[] distances;

    // is it a directed graph (true or false) :
    private boolean digraph;

    private int totalNodes;
     // all the nodes in the graph:
    private Vector<String> nodeList;

    private int totalEdges;    
     // all the adjacency lists, one for each node in the graph:
    private Vector<LinkedList<Integer>>  adjList;

    // all the weights of the edges, one for each node in the graph:
    private Vector<LinkedList<Integer>> adjWeight;
    
    // every visited node:
    private Vector<Boolean> visited;
    // list of nodes pre-visit:
    private Vector<Integer> nodeEnum;
    
    public AdjGraph() {
        init();
    }

    public AdjGraph(boolean ifdigraph) {
        init();
        digraph = ifdigraph;
    }

    public void init() {
        nodeList = new Vector<String>(); 
        adjList = new Vector<LinkedList<Integer>>(); 
        adjWeight = new Vector<LinkedList<Integer>>();
        visited = new Vector<Boolean>();
        nodeEnum = new Vector<Integer>();
        totalNodes = totalEdges = 0;
        digraph = false;
    }

    // set vertices
    public void setVertices(String[] nodes) {
        for (int i = 0; i < nodes.length; i ++) {
            nodeList.add(nodes[i]);
            adjList.add(new LinkedList<Integer>());
            adjWeight.add(new LinkedList<Integer>());
            visited.add(false);
            totalNodes ++;
        }
    }
    
    // add a vertex
    public void addVertex(String label) {
        nodeList.add(label);
        visited.add(false);
        adjList.add(new LinkedList<Integer>());
        adjWeight.add(new LinkedList<Integer>());
        totalNodes ++;
    }
    public int getNode(String node) {
        for(int i = 0; i < nodeList.size(); i ++) {
            if(nodeList.elementAt(i).equals(node)) return i;
        }
        return -1;
    }

    // return the number of vertices
    public int length() {
        return nodeList.size();
    }

    // add edge from v1 to v2:
    public void setEdge(int v1, int v2, int weight) {
        LinkedList<Integer> tmp = adjList.elementAt(v1);
        if(adjList.elementAt(v1).contains(v2) == false) {
            tmp.add(v2);
            adjList.set(v1,  tmp);
            totalEdges ++;
            LinkedList<Integer> tmp2 = adjWeight.elementAt(v1);
            tmp2.add(weight);
            adjWeight.set(v1,  tmp2);
        }
    }

    public void setEdge(String v1, String v2, int weight) {
        if ((getNode(v1) != -1) && (getNode(v2) != -1)) {
            // add edge from v1 to v2:
            setEdge(getNode(v1), getNode(v2), weight);
            // for undirected graphs, add edge from v2 to v1 as well:
            if (digraph == false) {
                setEdge(getNode(v2), getNode(v1), weight);
            }
        }
    }

    // keep track whether a vertex has been visited or not,
    //    for graph traversal purposes:
    public void setVisited(int v) {
        visited.set(v, true);
        nodeEnum.add(v);
    }

    public boolean ifVisited(int v) {
        return visited.get(v);
    }
    
    
        // new for Lab 18:
    public LinkedList<Integer> getNeighbors(int v) {
        return adjList.get(v);
    }

    public int getWeight(int v, int u) {
        LinkedList<Integer> tmp = getNeighbors(v);
        LinkedList<Integer> weight = adjWeight.get(v);
        if (tmp.contains(u)) {
            return weight.get(tmp.indexOf(u));
        } else {
            return Integer.MAX_VALUE;
        }
    }

    public void clearWalk() {
        nodeEnum.clear();
        for (int i = 0; i < nodeList.size(); i ++)
            visited.set(i, false);
    }

    public void walk(String method) {
        clearWalk();
        // traverse the graph:
        for (int i = 0; i < nodeList.size(); i ++) {
            if (ifVisited(i) == false) {
                if (method.equals("BFS")) BFS(i);      // i is the start node
                else if (method.equals("DFS")) DFS(i); // i is the start node
                else {
                    System.out.println("unrecognized traversal order: " + method);
                    System.exit(0);
                }
            }
        }
        System.out.println(method + ":");
        displayEnum();
    }

    public void relax(int start, int neigh) {
        int w = this.getWeight(start, neigh);
        if(distances[neigh] > distances[start] + w) {
            distances[neigh] = distances[start] + w;
        }
    }

    public void dijkstra(int s) {
        this.distances = new int[nodeList.size()];
        for(int i = 0; i < nodeList.size(); i++) {
            distances[i] = Integer.MAX_VALUE;
        }
        distances[s] = 0;

        for(int i = 0; i < nodeList.size(); i++) {
            int v = this.minVertex();
            this.setVisited(v);
            if(distances[v] == Integer.MAX_VALUE) {
                return;
            }
            for(int j = 0; j < adjList.get(v).size(); j++) {
                this.relax(v, adjList.get(v).get(j));
            }
            System.out.println(Arrays.toString(this.distances));
        }
    }

    public int minVertex() {
        int v = 0;
        for(int i = 0; i < nodeList.size(); i++) {
            if(!this.ifVisited(i)) {
                v = i;
                break;
            }
        }
        for(int i = 0; i < nodeList.size(); i++) {
            if(!this.ifVisited(i) && distances[i] < distances[v]) {
                v = i;
            }
        }
        return v;
    }
    
    public void DFS(int v) {
        setVisited(v);
        LinkedList<Integer> neighbors = adjList.elementAt(v);
        for(int i = 0; i < neighbors.size(); i ++) {
            int v1 = neighbors.get(i);
            if(ifVisited(v1) == false) DFS(v1); 
        }
    }
    public void BFS(int s) {
        ArrayList<Integer> toVisit = new ArrayList<Integer>();
        toVisit.add(s);
        while(toVisit.size() > 0) {
            int v = toVisit.remove(0); // first-in, first-visit
            setVisited(v);
            LinkedList<Integer> neighbors = adjList.elementAt(v);
            for(int i = 0; i < neighbors.size(); i ++) {
                int v1 = neighbors.get(i);
                if((ifVisited(v1) == false) && (toVisit.contains(v1) == false)) {
                    toVisit.add(v1);
                }
            }
        }
    }
    public void display() {
        System.out.println("total nodes: " + totalNodes);
        System.out.println("total edges: " + totalEdges);
    }
    public void displayEnum() {
        for(int i = 0; i < nodeEnum.size(); i ++) {
            System.out.print(nodeList.elementAt(nodeEnum.elementAt(i)) + " ");
        }
        System.out.println();
    }

    public void dijkstra2(int s) {
        clearWalk();
        int v;
        BinNode<Integer, Integer>[] nodes = new BinNode[totalNodes * totalNodes];
        nodes[0] = new BinNode(0, s);

        this.distances = new int[nodeList.size()];
        for(int i = 0; i < totalNodes; i++) {
            distances[i] = Integer.MAX_VALUE;
        }
        distances[s] = 0;

        for(int i = 1; i < nodes.length; i++) {
            nodes[i] = new BinNode(Integer.MAX_VALUE, i);
        }

        nodes[s].setKey(0);

        MinHeap<Integer,Integer> heap = new MinHeap(totalNodes * totalNodes, totalNodes, nodes);

        for(int i = 0; i < totalNodes; i++) {
            do {
                v = heap.removeMin().getValue();
            } while(ifVisited(v));
            setVisited(v);

            if(distances[v] == Integer.MAX_VALUE) {break;}
            for(int j = 0; j < adjList.get(v).size(); j++) {
                int start = v;
                int neigh = adjList.get(v).get(j);
                int w = this.getWeight(start, neigh);
                if(distances[neigh] > distances[start] + w) {
                    distances[neigh] = distances[start] + w;
                    heap.insert(new BinNode(distances[neigh], neigh));
                }
                System.out.println(Arrays.toString(this.distances));
            }
        }
    }

    public void topologicalSort() {
        clearWalk();
        LinkedList<Integer> q = new LinkedList<>();
        int[] count = new int[totalNodes];
        int v;

        for(v = 0; v < totalNodes; v++) {
            for(int w = 0; w < adjList.get(v).size(); w++) {
                count[adjList.get(v).get(w)]++;
            }
        }
        for(v = 0; v < totalNodes; v++) {
            if(count[v] == 0) {
                q.addLast(v);
            }
        }
        while(q.size() > 0) {
            v = q.removeFirst();
            System.out.print(v + " ");
            for(int w = 0; w < adjList.get(v).size(); w++) {
                int n = adjList.get(v).get(w);
                count[n]--;
                if(count[n] == 0) {
                    q.addLast(n);
                }
            }
        }
    }

    public static void main(String argv[]) {
        AdjGraph g1 = new AdjGraph();
        String[] nodes1 = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"};
        g1.setVertices(nodes1);
        g1.setEdge("A", "B", 1);
        g1.setEdge("B", "C", 2);
        g1.setEdge("C", "D", 3);
        g1.setEdge("A", "C", 2);
        g1.setEdge("C", "E", 2);
        g1.setEdge("C", "G", 2);
        g1.setEdge("G", "I", 2);

        g1.dijkstra2(1);
        System.out.println();

        AdjGraph g2 = new AdjGraph();
        String[] nodes2 = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"};
        g2.setVertices(nodes2);
        g2.setEdge("A", "B", 9);
        g2.setEdge("A", "F", 5);
        g2.setEdge("A", "E", 3);
        g2.setEdge("B", "C", 5);
        g2.setEdge("B", "F", 4);
        g2.setEdge("C", "D", 2);
        g2.setEdge("C", "F", 8);
        g2.setEdge("D", "F", 7);
        g2.setEdge("D", "E", 1);
        g2.setEdge("E", "F", 5);

        g2.dijkstra2(0);
        System.out.println();

        AdjGraph g3 = new AdjGraph();
        String[] nodes3 = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"};
        g3.setVertices(nodes3);
        g3.setEdge("A", "B", 5);
        g3.setEdge("A", "C", 4);
        g3.setEdge("A", "D", 3);
        g3.setEdge("A", "E", 2);
        g3.setEdge("E", "G", 1);
        g3.setEdge("E", "F", 2);
        g3.setEdge("E", "I", 3);
        g3.setEdge("I", "J", 4);

        g3.dijkstra2(2);
        System.out.println();

        AdjGraph g4 = new AdjGraph(true);
        String[] nodes4 = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"};
        g4.setVertices(nodes4);
        g4.setEdge("A", "C", 1);
        g4.setEdge("B", "C", 2);
        g4.setEdge("C", "D", 3);
        g4.setEdge("D", "E", 2);

        g4.setEdge("F", "G", 2);
        g4.setEdge("G", "H", 1);
        g4.setEdge("H", "I", 2);
        g4.setEdge("H", "J", 2);

        g4.topologicalSort();
        System.out.println();

        AdjGraph g5 = new AdjGraph(true);
        String[] nodes5 = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"};
        g5.setVertices(nodes5);
        g5.setEdge("H", "J", 1);
        g5.setEdge("H", "I", 1);
        g5.setEdge("H", "G", 1);
        g5.setEdge("G", "F", 1);
        g5.setEdge("F", "E", 1);
        g5.setEdge("E", "D", 1);
        g5.setEdge("D", "C", 1);
        g5.setEdge("C", "B", 1);
        g5.setEdge("C", "A", 1);

        g5.topologicalSort();
        System.out.println();

        AdjGraph g6 = new AdjGraph(true);
        String[] nodes6 = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"};
        g6.setVertices(nodes6);
        g6.setEdge("J", "I", 1);
        g6.setEdge("I", "H", 1);
        g6.setEdge("H", "G", 1);
        g6.setEdge("G", "F", 1);
        g6.setEdge("F", "E", 1);
        g6.setEdge("E", "D", 1);
        g6.setEdge("D", "C", 1);
        g6.setEdge("C", "B", 1);
        g6.setEdge("B", "A", 1);
        g6.setEdge("A", "J", 1);

        g6.topologicalSort(); // shouldn't print anything because it's a cycle

        AdjGraph g7 = new AdjGraph();
        String[] nodes7 = {"A", "B", "C", "D", "E", "F"};
        g7.setVertices(nodes7);
        g7.setEdge("A", "B", 10);
        g7.setEdge("A", "D", 20);
        g7.setEdge("A", "F", 2);
        g7.setEdge("B", "C", 3);
        g7.setEdge("B", "D", 5);
        g7.setEdge("C", "E", 15);
        g7.setEdge("D", "F", 10);
        g7.setEdge("D", "E", 11);
        g7.setEdge("E", "F", 3);

        g7.dijkstra2(0);
    }
}
