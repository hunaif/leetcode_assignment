class TrieNode:
    def __init__(self):
        self.dict = {}
        self.isWordEnd = False
        self.word = ''

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        found_words = []  #To store found words
        n_rows_board = len(board)
        n_cols_board = len(board[0])
        visited_nodes = [[False] * n_cols_board for _ in range(n_rows_board)]
        root = self.insertToTrie(words)

        for i in range(n_rows_board):
            for j in range(n_cols_board):
                self.search(i,j,root,n_rows_board,n_cols_board,board,visited_nodes,found_words)
        return found_words

    def search(self,i,j,root,n_rows_board,n_cols_board,board,visited_nodes,found_words):
        if(i<0 or i>=n_rows_board or
                j<0 or j>= n_cols_board or
                visited_nodes[i][j] == True):
            return
        if board[i][j] not in root.dict:
            return

        root = root.dict[board[i][j]]

        if root.isWordEnd:
            if root.word not in found_words:
                found_words.append(root.word)

        visited_nodes[i][j] = True
        to_visit = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
        for row,col in to_visit:
            self.search(row,col,root,n_rows_board,n_cols_board,board,visited_nodes,found_words)
        visited_nodes[i][j] = False

    def insertToTrie(self,words):
        root = TrieNode()

        for word in words:
            node = root
            for char in word:
                if char not in node.dict:
                    node.dict[char] = TrieNode()
                node = node.dict[char]

            node.isWordEnd = True
            node.word = word
        return root;