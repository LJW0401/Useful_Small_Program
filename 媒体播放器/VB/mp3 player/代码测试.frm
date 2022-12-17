VERSION 5.00
Begin VB.Form Form2 
   Caption         =   "代码测试"
   ClientHeight    =   3030
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   4560
   LinkTopic       =   "Form2"
   ScaleHeight     =   3030
   ScaleWidth      =   4560
   StartUpPosition =   3  '窗口缺省
   Begin VB.CommandButton Command1 
      Caption         =   "Command1"
      Height          =   855
      Left            =   2520
      TabIndex        =   1
      Top             =   840
      Width           =   1575
   End
   Begin VB.ListBox List1 
      Height          =   2400
      Left            =   120
      TabIndex        =   0
      Top             =   240
      Width           =   2175
   End
End
Attribute VB_Name = "Form2"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
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

Sub Model_Load_Lrc()
Dim i As Integer
Dim path0 As String
path0 = "E:\VB 工程项目\#项目\音乐播放器\music\语文\琵琶行 - 奇然,沈谧仁.lrc"
Open path0 For Input As 1
    Input #1, whole_lrc
Close #1
End Sub
Private Sub Command1_Click()
Dim i As Long, k As Integer, p As Integer
Dim ch As String, tmp As String
Dim flag As Boolean
Call Model_Load_Lrc
'=============
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
For i = 1 To lrc_num
    List1.AddItem CStr(lrc_time(i, 0)) & CStr(lrc_time(i, 1)) & lrc(i)
Next i
End Sub
