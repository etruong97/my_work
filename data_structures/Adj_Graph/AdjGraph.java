// C343 Summer 2019
//
// a simple implementation for graphs with adjacency lists

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Vector;

public class AdjGraph implements Graph {
    private boolean digraph;
    private int totalNode;
    private Vector<String> nodeList;
    private int totalEdge;
    private Vector<LinkedList<Integer>>  adjList;     // adjacency list
    private Vector<Boolean> visited;
    private Vector<Integer> nodeEnum;                 // list of nodes pre visit

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
        visited = new Vector<Boolean>();
        nodeEnum = new Vector<Integer>();
        totalNode = totalEdge = 0;
        digraph = false;
    }

    // set vertices:
    public void setVertices(String[] nodes) {
        for(int i = 0; i < nodes.length; i ++) {
            nodeList.add(nodes[i]);
            adjList.add(new LinkedList<Integer>());
            visited.add(false);
            totalNode ++;
        }
    }

    // add a vertex:
    public void addVertex(String label) {
        nodeList.add(label);
        visited.add(false);
        adjList.add(new LinkedList<Integer>());
        totalNode ++;
    }

    public int getNode(String node) {
        for(int i = 0; i < nodeList.size(); i ++) {
            if(nodeList.elementAt(i).equals(node)) return i;
        }
        return -1;
    }

    // return the number of vertices:
    public int length() {
        return nodeList.size();
    }

    // add edge from v1 to v2:
    public void setEdge(int v1, int v2, int weight) {
        LinkedList<Integer> tmp = adjList.elementAt(v1);
        if(adjList.elementAt(v1).contains(v2) == false) {
            tmp.add(v2);
            adjList.set(v1,  tmp);
            totalEdge ++;
        }
    }

    public void setEdge(String v1, String v2, int weight) {
        if((getNode(v1) != -1) && (getNode(v2) != -1)) {
            // add edge from v1 to v2
            setEdge(getNode(v1), getNode(v2), weight);
            // for undirected graphs, add edge from v2 to v1 as well
            if (digraph == false) setEdge(getNode(v2), getNode(v1), weight);
        }
    }

    // keep track if a vertex is visited or not, used e.g. for traversal:
    public void setVisited(int v) {
        visited.set(v, true);
        nodeEnum.add(v);
    }

    public boolean ifVisited(int v) {
        return visited.get(v);
    }

    public void clearWalk() {
        // clean up before traversing:
        nodeEnum.clear();
        for(int i = 0; i < nodeList.size(); i ++) visited.set(i, false);
    }

    public void walk(String method) {
        clearWalk();
        // traverse the graph
        for(int i = 0; i < nodeList.size(); i ++) {
            if(ifVisited(i) == false) {
                if(method.equals("BFS")) BFS(i);      // i is the start node
                else if(method.equals("DFS")) DFS(i); // i is the start node
                else {
                    System.out.println("unrecognized traversal order: " + method);
                    System.exit(0);
                }
            }
        }
        System.out.println(method + ":");
        displayEnum();
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
        System.out.println("total nodes: " + totalNode);
        System.out.println("total edges: " + totalEdge);
    }
    public void displayEnum() {
        for(int i = 0; i < nodeEnum.size(); i ++) {
            System.out.print(nodeList.elementAt(nodeEnum.elementAt(i)) + " ");
        }
        System.out.println();
    }

    // Lab 15 TODO:
    //
    // write your componentsAndSizes() method here.
    //

    public void componentsAndSizes() {
        int counter = 1;
        ArrayList<Integer> counterLs = new ArrayList<>();

        for(int i = 1; i < this.adjList.size(); i++) {
            if(this.adjList.elementAt(i-1).contains(i)) {
                counter++;
            }
            else {
                counterLs.add(counter);
                counter = 1;
            }
        }

        counterLs.add(counter);

        for(int i = 0; i < counterLs.size(); i++) {
            System.out.println("Component " + i + " has size " + counterLs.get(i));
        }
    }

    // Lab 15 TODO:

    // write a main() method here:

    // 1) instantiate a new graph,
    // 2) assign2 vertices and edges to the graph,
    // 3) then display2 the graph's content (use display() )
    // 4) finally call your componentsAndSizes() method to provide
    //    output results as from Lab 15 instructions

    // provide 3 different examples,
    //   with at least 10 nodes for each different graph
    public static void main(String[] args) {
        AdjGraph g1 = new AdjGraph();


        String[] str1 = new String[] {"a", "b", "c", "d", "e"};
        g1.setVertices(str1);
        g1.setEdge("a", "b", 0);
        g1.setEdge("b", "c", 0);
        g1.componentsAndSizes();

        System.out.println();

        AdjGraph g2 = new AdjGraph();
        String[] str2 = new String[] {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"};
        g2.setVertices(str2);
        g2.setEdge("a", "b", 1);
        g2.setEdge("b", "c", 1);
        g2.setEdge("c", "d", 1);
        g2.setEdge("a", "c", 1);
        g2.setEdge("a", "d", 1);
        g2.setEdge("e", "f", 1);
        g2.setEdge("e", "g", 1);
        g2.setEdge("f", "g", 1);
        g2.setEdge("g", "h", 1);
        g2.setEdge("g", "i", 1);
        g2.setEdge("g", "j", 1);
        g2.componentsAndSizes();

        System.out.println();

        AdjGraph g3 = new AdjGraph();
        String[] str3 = new String[] {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j"};
        g3.setVertices(str3);
        g3.setEdge("a", "b", 1);
        g3.setEdge("c", "d", 1);
        g3.setEdge("e", "f", 1);
        g3.setEdge("g", "h", 1);
        g3.setEdge("i", "j", 1);

        g3.componentsAndSizes();
    }
}
