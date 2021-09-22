class User:
    ranks = -8,-7,-6,-5,-4,-3,-2,-1,1,2, 3, 4, 5, 6, 7, 8
    lvl = 0
    rank = ranks[lvl]
    progress = 0
    def inc_progress(self, p_rank):
        ra = (self.lvl - self.ranks.index(p_rank)) * -1
        if(ra == -1):
            a = 1
        elif(ra == 0):
            a = 3
        elif(ra > 0):
            a_rank = self.ranks.index(p_rank)
            d = a_rank - self.lvl
            a = 10 * d * d
        elif(ra < -1):
            a = 0
        if(self.rank != 8 ):
            self.progress = self.progress + a
        else:
            a = 0
            
        if(self.progress >= 100):
            a_lvl = int(self.progress / 100)
            self.lvl += a_lvl
            if(self.lvl > 15):
                self.lvl = 15
            self.rank = self.ranks[self.lvl]
            self.progress = self.progress - (a_lvl * 100)
            
        if(self.rank == 8 ):
            self.progress = 0
