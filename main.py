import copy
import wx
import threading
from search import breadth_first_search, depth_fisrt_search


#code for the creation of the graphical ui
class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Missionaries and Cannibals',size=(500, 500))


        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL) #sizer who controls the size of all elements of the window

        self.text_ctrl = wx.TextCtrl(panel , value = "Missionaries and Cannibals Problem ", style = wx.TE_READONLY|wx.TE_CENTRE) #titles text box
        my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)

        #creation of bfs button and assignment to the sizer and a click event
        my_btn = wx.Button(panel, label='Run BFS')
        my_btn.Bind(wx.EVT_BUTTON, self.on_press_bfs)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)


        #creation of dfs button and assignment to the sizer and a click event
        my_btn1 = wx.Button(panel, label='Run DFS')
        my_btn1.Bind(wx.EVT_BUTTON, self.on_press_dfs)
        my_sizer.Add(my_btn1, 0, wx.ALL | wx.CENTER, 5)


        #text box for printing the problems solution
        self.text_ctr2 = wx.TextCtrl(panel, style = wx.TE_READONLY|wx.TE_MULTILINE|wx.TE_CENTRE,size=(300, 500))
        my_sizer.Add(self.text_ctr2, 0, wx.ALL | wx.EXPAND, 5)

        #assign the sizer to the panel
        panel.SetSizer(my_sizer)
        self.Show()


    #click events for the buttons
    def on_press_bfs(self, event):
        thread = threading.Thread(target=self.search_bfs) #starts new thread to not make ui unresponsive
        thread.start()


    def on_press_dfs(self,event):
        thread = threading.Thread(target=self.search_dfs) #starts new thread to not make ui unresponsive
        thread.start()


    #functions that calls the search algorithm and outputs the solution
    def search_dfs(self):
        solution1 , end_time = depth_fisrt_search()
        self.text_ctr2.Clear()
        self.text_ctr2.AppendText("Missionaries and Cannibals using Depth - First Search: \n")
        self.text_ctr2.AppendText(f"Completed in {end_time:0.4f} seconds. \n \n")
        path = [solution1]
        while solution1.parent:
            solution1 = solution1.parent
            path.append(solution1)
        self.text_ctr2.AppendText("                          " + "Left Side" + "                               " + "Right Side" + "                               " + "Boat \n")
        self.text_ctr2.AppendText(
            "          Cannibals" + "     Missionaries" + "       " + "Cannibals" + "       Missionaries" + "    Boat Position \n")
        counter = 0
        for p in reversed(path):
            self.text_ctr2.AppendText("State " + str(counter) + "    Left C: " + str(p.data["left"].cannibals) + ".    Left M: " + str(
                p.data["left"].missionaries) + ".     |   Right C: " + str(
                p.data["right"].cannibals) + ".     Right M: " + str(p.data["right"].missionaries) + ".     | Boat: " + str(
                p.data["boat"])+'\n')
            counter = counter + 1
        self.text_ctr2.AppendText("\n \n End of Path!")



    def search_bfs(self):
        solution , end_time = breadth_first_search()
        self.text_ctr2.Clear()
        self.text_ctr2.AppendText("Missionaries and Cannibals using Breadth - First Search: \n")
        self.text_ctr2.AppendText(f"Completed in {end_time:0.4f} seconds. \n \n")
        path = [solution]
        while solution.parent:
            solution = solution.parent
            path.append(solution)
        self.text_ctr2.AppendText("                          " + "Left Side" + "                               " + "Right Side" + "                               " + "Boat \n")
        self.text_ctr2.AppendText(
            "          Cannibals" + "     Missionaries" + "       " + "Cannibals" + "       Missionaries" + "    Boat Position \n")
        counter = 0
        for p in reversed(path):
            self.text_ctr2.AppendText("State " + str(counter) + "    Left C: " + str(p.data["left"].cannibals) + ".    Left M: " + str(
                p.data["left"].missionaries) + ".     |   Right C: " + str(
                p.data["right"].cannibals) + ".     Right M: " + str(p.data["right"].missionaries) + ".     | Boat: " + str(
                p.data["boat"])+'\n')
            counter = counter + 1
        self.text_ctr2.AppendText("\n \n End of Path!")





def main():
    print("Programm is Starting")


if __name__ == "__main__":
    main()
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()
