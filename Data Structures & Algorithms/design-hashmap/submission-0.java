class MyHashMap {

    private final int MAX_KEY = 1_000_000;
    private final int[] vals;
    private final boolean[] present;

    public MyHashMap() {
        vals = new int[MAX_KEY + 1];
        present = new boolean[MAX_KEY + 1];
    }
    
    public void put(int key, int value) {
        if (key < 0 || key > MAX_KEY) return; // defensive, not strictly required by constraints
        vals[key] = value;
        present[key] = true;
    }
    
    public int get(int key) {
        if (key < 0 || key > MAX_KEY) return -1;
        return present[key] ? vals[key] : -1;
    }
    
    public void remove(int key) {
        if (key < 0 || key > MAX_KEY) return;
        present[key] = false;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */