def solution(begin, target, words):
    #words안에 target이 없으면 0을 리턴해.
    if target not in words:
        return 0
        
    def build_graph(words):
        graph = {}
        for word in words:
            graph[word] = []
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    if char != word[i]:
                        possible_word = word[:i] + char + word[i+1:]
                        if possible_word in words:
                            graph[word].append(possible_word)
                            
        return graph
    
    word_set = set(words)
    word_set.add(begin)
    graph = build_graph(word_set)
    
    queue = [(begin, 0)]
    visited = {begin}
    
    
    while queue:
        current_word, steps = queue.pop(0)
        
        for neighbor in graph.get(current_word, []):
            if neighbor == target:
                return steps +1
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps +1))
                
    return 0