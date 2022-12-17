VERSION 5.00
Object = "{6BF52A50-394A-11D3-B153-00C04F79FAA6}#1.0#0"; "wmp.dll"
Begin VB.Form Form1 
   Caption         =   "小小音乐播放器"
   ClientHeight    =   3375
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   6585
   Icon            =   "音乐播放器.frx":0000
   LinkTopic       =   "Form1"
   MaxButton       =   0   'False
   ScaleHeight     =   3375
   ScaleWidth      =   6585
   StartUpPosition =   3  '窗口缺省
   Begin VB.Timer Timer2 
      Interval        =   10
      Left            =   5640
      Top             =   720
   End
   Begin VB.Frame Frame2 
      Height          =   615
      Left            =   0
      TabIndex        =   10
      Top             =   2760
      Width           =   6615
      Begin WMPLibCtl.WindowsMediaPlayer WindowsMediaPlayer1 
         Height          =   960
         Left            =   0
         TabIndex        =   11
         Top             =   120
         Width           =   6615
         URL             =   ""
         rate            =   1
         balance         =   0
         currentPosition =   0
         defaultFrame    =   ""
         playCount       =   1
         autoStart       =   -1  'True
         currentMarker   =   0
         invokeURLs      =   -1  'True
         baseURL         =   ""
         volume          =   50
         mute            =   0   'False
         uiMode          =   "full"
         stretchToFit    =   0   'False
         windowlessVideo =   0   'False
         enabled         =   -1  'True
         enableContextMenu=   -1  'True
         fullScreen      =   0   'False
         SAMIStyle       =   ""
         SAMILang        =   ""
         SAMIFilename    =   ""
         captioningID    =   ""
         enableErrorDialogs=   0   'False
         _cx             =   11668
         _cy             =   1693
      End
   End
   Begin VB.Frame Frame1 
      Height          =   735
      Left            =   2280
      TabIndex        =   9
      Top             =   2040
      Width           =   2295
      Begin VB.Image Image3 
         Height          =   495
         Left            =   120
         Picture         =   "音乐播放器.frx":10CA
         Top             =   120
         Width           =   495
      End
      Begin VB.Image Image2 
         Height          =   495
         Left            =   1680
         Picture         =   "音乐播放器.frx":1488
         Top             =   120
         Width           =   495
      End
      Begin VB.Image Image1 
         Height          =   570
         Left            =   840
         Picture         =   "音乐播放器.frx":1853
         Top             =   120
         Width           =   570
      End
   End
   Begin VB.ComboBox Combo3 
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   10.5
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   330
      Left            =   1320
      TabIndex        =   8
      Top             =   1560
      Width           =   5175
   End
   Begin VB.HScrollBar HScroll1 
      Height          =   255
      LargeChange     =   10
      Left            =   1560
      Max             =   100
      TabIndex        =   6
      Top             =   1200
      Value           =   5
      Width           =   3615
   End
   Begin VB.TextBox Text1 
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   14.25
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   840
      TabIndex        =   5
      Text            =   "5"
      Top             =   1080
      Width           =   615
   End
   Begin VB.ComboBox Combo2 
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   14.25
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   405
      Left            =   1320
      TabIndex        =   3
      Text            =   "列表循环"
      Top             =   600
      Width           =   3855
   End
   Begin VB.ComboBox Combo1 
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   14.25
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   405
      Left            =   1320
      TabIndex        =   0
      Top             =   120
      Width           =   3855
   End
   Begin VB.Timer Timer1 
      Left            =   6000
      Top             =   120
   End
   Begin VB.Label Label5 
      Alignment       =   2  'Center
      Caption         =   "Label5 歌词"
      Height          =   375
      Left            =   120
      TabIndex        =   12
      Top             =   3720
      Width           =   6255
   End
   Begin VB.Label Label4 
      Caption         =   "播放列表："
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   14.25
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   0
      TabIndex        =   7
      Top             =   1560
      Width           =   1575
   End
   Begin VB.Label Label3 
      Caption         =   "音量："
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   14.25
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   0
      TabIndex        =   4
      Top             =   1080
      Width           =   1335
   End
   Begin VB.Label Label2 
      Caption         =   "播放模式："
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   14.25
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   495
      Left            =   0
      TabIndex        =   2
      Top             =   600
      Width           =   2175
   End
   Begin VB.Label Label1 
      Caption         =   "选择歌单："
      BeginProperty Font 
         Name            =   "宋体"
         Size            =   14.25
         Charset         =   134
         Weight          =   400
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   375
      Left            =   0
      TabIndex        =   1
      Top             =   120
      Width           =   1695
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
'添加windowsmediaplayer控件 一个timer控件即可使用
Option Explicit
Dim list2() As String, B可播放文件数 As Integer '可以播放的文件
Dim list() As String '存放所有的文件名
Dim total As Long '文件总个数
Dim now As Long '用来记录当前读取的文件的排序
Dim allname() As String
Dim path1 As String
Dim play As Boolean
Dim f_lrc As Boolean
Dim whole_lrc As String
Dim lrc() As String, lrc_num As Integer
Dim lrc_time() As Integer

Sub add_lrc()
Dim i As Long, k As Integer, p As Integer
Dim ch As String, tmp As String
Dim flag As Boolean
lrc_num = 0
For i = 1 To Len(whole_lrc)
    ch = Mid(whole_lrc, i, 1)
    If ch = "[" Then
        flag = False
        k = k + 1
        p = 0
        lrc_num = lrc_num + 1
        ReDim lrc_time(k, 1)
        ReDim Preserve lrc(k)
    ElseIf ch = "]" Then
        flag = True
        lrc_time(k, 1) = Int(Val(tmp))
    Else
        If flag Then
            lrc(k) = lrc(k) & ch
        Else
            If ch = ":" Then
                lrc_time(k, 0) = Int(Val(tmp))
            Else
                tmp = tmp & ch
            End If
        End If
    End If
Next i
'For i = 1 To lrc_num
'    List1.AddItem CStr(lrc_time(i, 0)) & CStr(lrc_time(i, 1)) & lrc(i)
'Next i
End Sub

Sub Model_Load_Lrc()
Dim i As Integer
Dim path0 As String
f_lrc = False
For i = 1 To total
    If list(i) = list2(now) Then
        path0 = Mid(list(i), 1, Len(list(i)) - 3) & "lrc"
        If list(i - 1) = Mid(list(i), 1, Len(list(i)) - 3) & "lrc" Then
            f_lrc = True
            Open list(i) For Input As 1
                Input #1, whole_lrc
            Close #1
        End If
    End If
    If f_lrc Then
        Exit For
    End If
Next i
If Not f_lrc Then
    Label5.Caption = ""
Else
    Call add_lrc
End If
End Sub
Sub Model_Show_Lrc()
If f_lrc Then
    
End If
End Sub
Sub play1() '列表循环
    If Me.WindowsMediaPlayer1.playState = wmppsStopped Then
        now = now + 1
        If now > B可播放文件数 Then now = 1
        Me.WindowsMediaPlayer1.URL = list2(now)
        Me.WindowsMediaPlayer1.Controls.play
        Combo3.Text = allname(now)
    End If
End Sub
Sub play2() '随机播放
    If Me.WindowsMediaPlayer1.playState = wmppsStopped Then
        Randomize
        now = Int(Rnd * (B可播放文件数) + 1)
        Me.WindowsMediaPlayer1.URL = list2(now)
        Me.WindowsMediaPlayer1.Controls.play
        Combo3.Text = allname(now)
    End If
End Sub
Sub play3() '单曲循环
    If Me.WindowsMediaPlayer1.playState = wmppsStopped Then
        Me.WindowsMediaPlayer1.URL = list2(now)
        Me.WindowsMediaPlayer1.Controls.play
    End If
End Sub
Sub play4() '顺序播放
    If Me.WindowsMediaPlayer1.playState = wmppsStopped Then
        now = now + 1
        If now <= B可播放文件数 Then
            Me.WindowsMediaPlayer1.URL = list2(now)
            Me.WindowsMediaPlayer1.Controls.play
            Combo3.Text = allname(now)
        End If
    End If
End Sub
Private Sub Combo1_Click()
path1 = "\music\" & Combo1.Text
play = True
Combo3.Clear
    now = 1
    total = 0
    getAll App.Path & path1 '指定音乐文件夹
    '输出文件的个数
    Call F存入可播放文件名
    If B可播放文件数 > 0 Then
        Me.WindowsMediaPlayer1.URL = list2(now)
        Image1.Picture = LoadPicture(App.Path & "\picture\暂停2.jpg")
        Combo3.Text = allname(now)
    Else
        MsgBox "没有音乐文件"
    End If
End Sub
Private Sub Combo3_Click()
Dim i As Integer
For i = 1 To B可播放文件数
    If allname(i) = Combo3.Text Then now = i: Exit For
Next i
Me.WindowsMediaPlayer1.URL = list2(now)
Me.WindowsMediaPlayer1.Controls.play
End Sub

Private Sub Form_Load()
Dim i As Integer, k As Integer
Dim tmp(10) As String
play = False
WindowsMediaPlayer1.settings.volume = Val(Text1.Text)
Timer1.Interval = 200

Open App.Path & "\List.txt" For Input As 1
Input #1, k
For i = 0 To k
    Input #1, tmp(i)
    Combo1.AddItem tmp(i)
Next i
Close #1
Combo2.AddItem "列表循环"
Combo2.AddItem "随机播放"
Combo2.AddItem "单曲循环"
Combo2.AddItem "顺序播放"

'Form2.Show '测试

End Sub
Private Sub HScroll1_Change()
WindowsMediaPlayer1.settings.volume = HScroll1.Value
Text1.Text = CStr(HScroll1.Value)
End Sub
Private Sub Image1_Click()
    If Me.WindowsMediaPlayer1.playState = wmppsPlaying Then
        Image1.Picture = LoadPicture(App.Path & "\picture\开始2.jpg")
        WindowsMediaPlayer1.Controls.pause
    ElseIf play Then
        Image1.Picture = LoadPicture(App.Path & "\picture\暂停2.jpg")
        WindowsMediaPlayer1.Controls.play
    End If
End Sub
Private Sub Image2_Click()
    now = now + 1
    If now > B可播放文件数 Then now = 1
    Me.WindowsMediaPlayer1.URL = list2(now)
    Me.WindowsMediaPlayer1.Controls.play
    Combo3.Text = allname(now)
End Sub
Private Sub Image3_Click()
    now = now - 1
    If now <= 0 Then now = B可播放文件数
    Me.WindowsMediaPlayer1.URL = list2(now)
    Me.WindowsMediaPlayer1.Controls.play
    Combo3.Text = allname(now)
End Sub
Private Sub Text1_Change()
If Val(Text1.Text) <= 100 And Val(Text1.Text) >= 0 Then
    WindowsMediaPlayer1.settings.volume = Val(Text1.Text)
    HScroll1.Value = Val(Text1.Text)
End If
End Sub
Private Sub Timer1_Timer()
    If Combo2.Text = "列表循环" Then
        Call play1
    ElseIf Combo2.Text = "随机播放" Then
        Call play2
    ElseIf Combo2.Text = "单曲循环" Then
        Call play3
    ElseIf Combo2.Text = "顺序播放" Then
        Call play4
    End If
    If Val(Text1.Text) <> WindowsMediaPlayer1.settings.volume Then Text1.Text = CStr(WindowsMediaPlayer1.settings.volume)
    If Me.WindowsMediaPlayer1.playState = wmppsStopped Then Image1.Picture = LoadPicture(App.Path & "\picture\开始2.jpg")
End Sub
'遍历指定目录下的文件 并将所有的文件名放入数组list
Function getAll(rootF)
    Dim fso As Object, folder As Object, subfolder As Object, file As Object
    Set fso = CreateObject("scripting.filesystemobject") '创建FSO对象
    Set folder = fso.getfolder(rootF) '得到文件夹对象
    For Each subfolder In folder.subfolders '遍历子文件夹
        Call getAll(subfolder) '递归,查找该文件夹的子文件夹
    Next
    For Each file In folder.Files '遍历根文件夹下的文件
        Debug.Print folder
        Debug.Print file '输出文件名
        total = total + 1
        ReDim Preserve list(total) As String
        list(total) = file
    Next
    Set fso = Nothing
    Set folder = Nothing
    Set fso = Nothing
End Function
Function F存入可播放文件名()
    Dim i As Integer
    B可播放文件数 = 0
    For i = 1 To total
        If Right$(list(i), 3) = "mp3" Or Right$(list(i), 3) = "wav" Then
            B可播放文件数 = B可播放文件数 + 1
            ReDim Preserve list2(B可播放文件数)
            list2(B可播放文件数) = list(i)
            
            Combo3.AddItem deal(list(i)) '添加歌曲名
            ReDim Preserve allname(B可播放文件数)
            allname(B可播放文件数) = deal(list(i))
        End If
    Next
End Function
Function deal(txt As String) As String
Dim i As Integer, k As Integer
Dim flag As Boolean, flag2 As Boolean
Dim ch As String
Dim a(1 To 15) As String '放文件夹
flag = False
k = 1
For i = 1 To Len(txt)
    ch = Mid(txt, i, 1)
    If ch = "\" Then k = k + 1 Else a(k) = a(k) & ch
Next i
deal = a(k)
End Function
