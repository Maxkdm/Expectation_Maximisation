import random
import time
import sys

class Graph_Node:
    def __init__(self, name, n, vals):
        self.Node_Name = name
        self.nvalues = n
        self.values = vals
        self.Children = []
        self.Parents = []
        self.CPT = {}
        self.evidence = ""
        self.freq = {}

    def get_name(self):
        return self.Node_Name

    def get_children(self):
        return self.Children

    def get_Parents(self):
        return self.Parents

    def get_CPT(self):
        return self.CPT

    def get_nvalues(self):
        return self.nvalues

    def get_values(self):
        return self.values

    def set_CPT(self, new_CPT,data):
        self.CPT[new_CPT] = data

    def set_Parents(self, Parent_Nodes):
        self.Parents = Parent_Nodes

    def add_child(self, new_child_index):
        if new_child_index not in self.Children:
            self.Children.append(new_child_index)
            return 1
        return 0

    def evidence_t(self):
        return self.evidence

    def give_evidence(self,some):
        self.evidence = some

    def set_freq(self,tup,valuer):
        self.freq[tup] = valuer

    def get_freq(self):
        return self.freq

    def set_freq_parent(self,tup,valuer):
        self.freq[tup] = valuer

    def get_freq_parent(self):
        return self.freq



class Network:
    def __init__(self):
        self.Pres_Graph = []

    def addNode(self, node):
        node = Graph_Node(node.get_name(), node.get_nvalues(), node.get_values())
        self.Pres_Graph.append(node)
        return 0


    def get_nth_node(self, n):
        if 0 <= n < len(self.Pres_Graph):
            return self.Pres_Graph[n]
        return None


def read_network():

    global name_nodes
    name_nodes = []
    with open(sys.argv[1], "r") as file:

        cont = file.readline()
        while cont:
            cut = cont.strip()
            de = cut.split(" ")
            if de[0]=="variable":
                curl = de.index("{")
                ls  = de[1:curl]
                for i in range(len(ls)):
                    if ls[i]!= " ":
                        name = ls[i]

                name_nodes.append(name)

            elif de[0]=="type":
                bracket_st = de.index("{")
                bracket_end = de.index("};")
                lsk = de[bracket_st+1:bracket_end]
                var_list = []
                var = 0

                for i in range(len(lsk)):
                    if lsk[i]!= "":
                        var+= 1
                        var_list.append(lsk[i])


                alarm.addNode(Graph_Node(name_nodes[-1],var,var_list))


            elif de[0]=="probability":
                brack_st = de.index("(")
                brack_end = de.index(")")
                mnb = de[brack_st+1:brack_end]
                prob_tab = []

                for i in range(len(mnb)):

                    if mnb[i]!= '':
                        loc1 = name_nodes.index(mnb[i])
                        prob_tab.append(loc1)
                if len(prob_tab)==1:
                    X = alarm.get_nth_node(prob_tab[0])

                    ken = X.get_nvalues()

                    for t in range(ken):
                        X.set_CPT((X.get_values()[t],), random.uniform(0.0001, 0.9999))
                        X.set_freq((X.get_values()[t],),1)


                elif len(prob_tab)==2:
                    X = alarm.get_nth_node(prob_tab[0])
                    Y = alarm.get_nth_node(prob_tab[1])
                    ken1 = alarm.get_nth_node(prob_tab[0]).get_nvalues()
                    ken2 = alarm.get_nth_node(prob_tab[1]).get_nvalues()

                    for r in range(ken1):
                        for t in range(ken2):
                            X.set_CPT((X.get_values()[r],Y.get_values()[t]), random.uniform(0.0001, 0.9999))
                            X.set_freq((X.get_values()[r],Y.get_values()[t]),0.1)
                            X.set_freq_parent((Y.get_values()[t],),1)


                    X.set_Parents([prob_tab[1]])
                    Y.add_child((prob_tab[0]))

                elif len(prob_tab)==3:
                    X = alarm.get_nth_node(prob_tab[0])
                    Y = alarm.get_nth_node(prob_tab[1])
                    Z = alarm.get_nth_node(prob_tab[2])
                    ken1 = X.get_nvalues()
                    ken2 = Y.get_nvalues()
                    ken3 = Z.get_nvalues()

                    for r in range(ken1):
                        for t in range(ken2):
                            for s in range(ken3):
                                X.set_CPT((X.get_values()[r],Y.get_values()[t],Z.get_values()[s]) ,random.uniform(0.0001, 0.9999))
                                X.set_freq((X.get_values()[r],Y.get_values()[t],Z.get_values()[s]),0.1)
                                X.set_freq_parent((Y.get_values()[t],Z.get_values()[s]),1)

                    X.set_Parents([prob_tab[1],prob_tab[2]])
                    Y.add_child((prob_tab[0]))
                    Z.add_child((prob_tab[0]))

                elif len(prob_tab)==4:
                    X = alarm.get_nth_node(prob_tab[0])
                    Y = alarm.get_nth_node(prob_tab[1])
                    Z = alarm.get_nth_node(prob_tab[2])
                    W = alarm.get_nth_node(prob_tab[3])
                    ken1 = X.get_nvalues()
                    ken2 = Y.get_nvalues()
                    ken3 = Z.get_nvalues()
                    ken4 = W.get_nvalues()

                    for r in range(ken1):
                        for t in range(ken2):
                            for s in range(ken3):
                                for q in range(ken4):
                                    X.set_CPT((X.get_values()[r],Y.get_values()[t],Z.get_values()[s],W.get_values()[q]) ,random.uniform(0.0001, 0.9999))
                                    X.set_freq((X.get_values()[r],Y.get_values()[t],Z.get_values()[s],W.get_values()[q]),0.1)
                                    X.set_freq_parent((Y.get_values()[t],Z.get_values()[s],W.get_values()[q]),1)

                    X.set_Parents([prob_tab[1],prob_tab[2],prob_tab[3]])
                    Y.add_child((prob_tab[0]))
                    Z.add_child((prob_tab[0]))
                    W.add_child((prob_tab[0]))

                elif len(prob_tab)==5:
                    X = alarm.get_nth_node(prob_tab[0])
                    Y = alarm.get_nth_node(prob_tab[1])
                    Z = alarm.get_nth_node(prob_tab[2])
                    W = alarm.get_nth_node(prob_tab[3])
                    V = alarm.get_nth_node(prob_tab[4])
                    ken1 = X.get_nvalues()
                    ken2 = Y.get_nvalues()
                    ken3 = Z.get_nvalues()
                    ken4 = W.get_nvalues()
                    ken5 = V.get_nvalues()

                    for r in range(ken1):
                        for t in range(ken2):
                            for s in range(ken3):
                                for q in range(ken4):
                                    for p in range(ken5):
                                        X.set_CPT((X.get_values()[r],Y.get_values()[t],Z.get_values()[s],W.get_values()[q],V.get_values()[p]) ,random.uniform(0.0001, 0.9999))
                                        X.set_freq((X.get_values()[r],Y.get_values()[t],Z.get_values()[s],W.get_values()[q],V.get_values()[p]), 1)
                                        X.set_freq_parent((Y.get_values()[t],Z.get_values()[s],W.get_values()[q],V.get_values()[p]),0.1)

                    X.set_Parents([prob_tab[1],prob_tab[2],prob_tab[3],prob_tab[4]])
                    Y.add_child((prob_tab[0]))
                    Z.add_child((prob_tab[0]))
                    W.add_child((prob_tab[0]))
                    V.add_child((prob_tab[0]))

            cont = file.readline()


def pr(L):
    J = []

    if len(L)==1:
        U1 = (L[0].evidence_t(),)
        return L[0].get_CPT()[U1]
    else:
        for i in range(len(L)):

            J.append(L[i].evidence_t())
        j0 = tuple(J)

        return L[0].get_CPT()[j0]


def markov_blanket_sampling(node_name):

    child = node_name.get_children()

    parent = node_name.get_Parents()
    n = []
    prev = 0
    n0 = []
    res = node_name.get_values()[0]
    for i in range(len(child)):

        s = alarm.get_nth_node(child[i]).get_Parents()

        for fd in range(len(s)):
            n0.append(alarm.get_nth_node(s[fd]))
        n1 = [alarm.get_nth_node(child[i])] + n0
        n.append(n1)
        n0 = []

    lad = [node_name]
    if len(parent)!=0:
        for i in range(len(parent)):
            lad.append(alarm.get_nth_node(parent[i]))
    for i in range(node_name.nvalues):
        node_name.give_evidence(node_name.get_values()[i])
        va = pr(lad)

        for k in range(len(child)):
            va*= pr(n[k])
        if va>prev:
            prev = va
            res = node_name.get_values()[i]
    return res



def expectation():


    with open(sys.argv[2],  "r") as file:
        line = file.readline()
        missing_factor = None
        while line:
            fg1 = line.split("\n")
            fg = fg1[0].split(" ")


            for i in range(len(fg)):
                if fg[i] != '"?"':

                    alarm.get_nth_node(i).give_evidence(fg[i])
                elif fg[i] == '"?"':

                    missing_factor = i

            if missing_factor != None:
                md = markov_blanket_sampling(alarm.get_nth_node(missing_factor))

                alarm.get_nth_node(missing_factor).give_evidence(md)

            for i in range(len(fg)):
                A = alarm.get_nth_node(i).get_Parents()
                N = []
                for l in range(len(A)):
                    N.append(alarm.get_nth_node(A[l]))

                S = [alarm.get_nth_node(i)] + N

                jh = []
                for g in range(len(N)):
                    jh.append((N[g]).evidence_t())
                xc = []
                for h in range(len(S)):
                    xc.append((S[h]).evidence_t())
                xc1 = tuple(xc)
                if jh != []:
                    jh1 = tuple(jh)
                    alarm.get_nth_node(i).get_freq()[xc1]+=1
                    alarm.get_nth_node(i).get_freq_parent()[jh1]+=1
                else:
                    alarm.get_nth_node(i).get_freq()[xc1] += 1



            line = file.readline()



def maximisation():
    for b in range(len(name_nodes)):
        k = alarm.get_nth_node(b).get_CPT()
        for j in k.keys():
            if (len(alarm.get_nth_node(b).get_Parents())==0):
                k[j] = float("{:.4f}".format(alarm.get_nth_node(b).get_freq()[j]/sum(alarm.get_nth_node(b).get_freq().values())))

            else:
                k[j] = float("{:.4f}".format(alarm.get_nth_node(b).get_freq()[j]/alarm.get_nth_node(b).get_freq_parent()[j[1:]]))
                

def EM_algo():


    counter = 0

    while True:
        end = time.time()
        if end-start >= 115:
            break
        expectation()

        old_cpt = []
        for i in range(len(name_nodes)):
            for j in (alarm.get_nth_node(i).get_CPT().keys()):
                old_cpt.append(alarm.get_nth_node(i).get_CPT()[j])
        maximisation()
        new_cpt = []
        for o in range(len(name_nodes)):
            for u in (alarm.get_nth_node(o).get_CPT().keys()):
                new_cpt.append(alarm.get_nth_node(o).get_CPT()[u])

        diff = []
        for g in range(len(old_cpt)):

            diff.append(abs(old_cpt[g]-new_cpt[g]))
        ter = max(diff)
        print(ter)
        if ter<0.0002:
            break
        counter+= 1
        # print(counter)
    

    return alarm

def exit(alarm):

    with open('solved_alarm.bif', 'w') as output, open('alarm.bif', 'r') as input:
        qe = 0
        line = input.readline()
        while line:
            lex = line.strip()
            lex1 = lex.split(" ")
            if lex1[0]=='table':

                D = alarm.get_nth_node(qe).get_CPT()
                gfh = ""
                for key in D.keys():
                    gfh += str(D[key])+" "
                gfh = "    " + "table" + " " + gfh + ";" + "\n"
                output.write(gfh)
                qe+=1
            else:

                output.write(line)

            line = input.readline()
    last = time.time()
    print(last-start)




if __name__ == "__main__":
    start = time.time()
    alarm = Network()
    read_network()
    print("done initialising")
    EM_algo()
    exit(alarm)
    print("finished writing")


