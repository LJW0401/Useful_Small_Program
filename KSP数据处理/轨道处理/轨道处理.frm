VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "轨道运算"
   ClientHeight    =   3960
   ClientLeft      =   120
   ClientTop       =   450
   ClientWidth     =   7455
   LinkTopic       =   "Form1"
   ScaleHeight     =   3960
   ScaleWidth      =   7455
   StartUpPosition =   3  '窗口缺省
   Begin VB.Frame Frame4 
      Caption         =   "轨道ap,ep参数"
      Height          =   1335
      Left            =   3600
      TabIndex        =   41
      Top             =   2520
      Width           =   3735
      Begin VB.TextBox Text11 
         Height          =   270
         Left            =   600
         TabIndex        =   48
         Text            =   "Text11"
         Top             =   960
         Width           =   2535
      End
      Begin VB.TextBox Text10 
         Height          =   270
         Left            =   600
         TabIndex        =   47
         Text            =   "Text10"
         Top             =   720
         Width           =   2535
      End
      Begin VB.TextBox Text9 
         Height          =   270
         Left            =   360
         TabIndex        =   43
         Text            =   "Text9"
         Top             =   240
         Width           =   2775
      End
      Begin VB.Label Unit 
         Caption         =   "(m)"
         Height          =   255
         Index           =   11
         Left            =   3120
         TabIndex        =   50
         Top             =   960
         Width           =   375
      End
      Begin VB.Label Unit 
         Caption         =   "(m)"
         Height          =   255
         Index           =   10
         Left            =   3120
         TabIndex        =   49
         Top             =   720
         Width           =   375
      End
      Begin VB.Label Label19 
         Caption         =   "Ep >"
         ForeColor       =   &H000080FF&
         Height          =   255
         Left            =   120
         TabIndex        =   46
         Top             =   960
         Width           =   2655
      End
      Begin VB.Label Label18 
         Caption         =   "Ap >"
         ForeColor       =   &H000080FF&
         Height          =   255
         Left            =   120
         TabIndex        =   45
         Top             =   720
         Width           =   2655
      End
      Begin VB.Label Unit 
         Caption         =   "(s)"
         Height          =   255
         Index           =   9
         Left            =   3120
         TabIndex        =   44
         Top             =   240
         Width           =   375
      End
      Begin VB.Label Label17 
         Caption         =   "T="
         Height          =   375
         Left            =   120
         TabIndex        =   42
         Top             =   240
         Width           =   735
      End
   End
   Begin VB.Frame Frame3 
      Caption         =   "星球数据"
      Height          =   1095
      Left            =   120
      TabIndex        =   19
      Top             =   120
      Width           =   3375
      Begin VB.TextBox Text7 
         Height          =   270
         Left            =   1920
         TabIndex        =   36
         Text            =   "Text7"
         Top             =   480
         Width           =   615
      End
      Begin VB.TextBox Text6 
         Height          =   270
         Left            =   1080
         TabIndex        =   34
         Text            =   "Text6"
         Top             =   480
         Width           =   615
      End
      Begin VB.TextBox R_R 
         Height          =   270
         Left            =   1080
         TabIndex        =   21
         Text            =   "Text3"
         Top             =   240
         Width           =   1575
      End
      Begin VB.Label Unit 
         Caption         =   "kg*m/s^2"
         Height          =   255
         Index           =   7
         Left            =   2520
         TabIndex        =   37
         Top             =   480
         Width           =   735
      End
      Begin VB.Label Label15 
         Caption         =   "E+"
         Height          =   255
         Left            =   1680
         TabIndex        =   35
         Top             =   480
         Width           =   615
      End
      Begin VB.Label Label14 
         Caption         =   "星球GM参数"
         Height          =   255
         Left            =   120
         TabIndex        =   33
         Top             =   480
         Width           =   1215
      End
      Begin VB.Label Unit 
         Caption         =   "(km)"
         Height          =   255
         Index           =   0
         Left            =   2640
         TabIndex        =   22
         Top             =   240
         Width           =   375
      End
      Begin VB.Label Label8 
         Caption         =   "星球半径R"
         Height          =   255
         Left            =   120
         TabIndex        =   20
         Top             =   240
         Width           =   975
      End
   End
   Begin VB.Frame Frame2 
      Caption         =   "轨道周期"
      Height          =   2535
      Left            =   120
      TabIndex        =   18
      Top             =   1320
      Width           =   3375
      Begin VB.TextBox Text8 
         Height          =   270
         Left            =   360
         TabIndex        =   38
         Text            =   "Text8"
         Top             =   1560
         Width           =   2295
      End
      Begin VB.TextBox Text5 
         Height          =   270
         Left            =   360
         TabIndex        =   32
         Text            =   "Text5"
         Top             =   1320
         Width           =   2295
      End
      Begin VB.TextBox Text4 
         Height          =   270
         Left            =   360
         TabIndex        =   27
         Text            =   "Text4"
         Top             =   720
         Width           =   2295
      End
      Begin VB.TextBox Text3 
         Height          =   270
         Left            =   360
         TabIndex        =   26
         Text            =   "Text3"
         Top             =   480
         Width           =   2295
      End
      Begin VB.Label Unit 
         Caption         =   "(s)"
         Height          =   255
         Index           =   8
         Left            =   2640
         TabIndex        =   39
         Top             =   1320
         Width           =   375
      End
      Begin VB.Label Label13 
         Caption         =   "T="
         ForeColor       =   &H000080FF&
         Height          =   495
         Left            =   120
         TabIndex        =   31
         Top             =   1320
         Width           =   2895
      End
      Begin VB.Label Label12 
         Caption         =   "轨道周期"
         Height          =   255
         Left            =   120
         TabIndex        =   30
         Top             =   1080
         Width           =   855
      End
      Begin VB.Label Unit 
         Caption         =   "(m)"
         Height          =   255
         Index           =   6
         Left            =   2640
         TabIndex        =   29
         Top             =   720
         Width           =   375
      End
      Begin VB.Label Unit 
         Caption         =   "(m)"
         Height          =   255
         Index           =   5
         Left            =   2640
         TabIndex        =   28
         Top             =   480
         Width           =   375
      End
      Begin VB.Label Label11 
         Caption         =   "Ep"
         Height          =   375
         Left            =   120
         TabIndex        =   25
         Top             =   720
         Width           =   735
      End
      Begin VB.Label Label9 
         Caption         =   "Ap"
         Height          =   255
         Left            =   120
         TabIndex        =   24
         Top             =   480
         Width           =   495
      End
      Begin VB.Label Label1 
         Caption         =   "轨道数据"
         Height          =   375
         Left            =   120
         TabIndex        =   23
         Top             =   240
         Width           =   1935
      End
   End
   Begin VB.Frame Frame1 
      Caption         =   "共振轨道"
      Height          =   2295
      Left            =   3600
      TabIndex        =   0
      Top             =   120
      Width           =   3735
      Begin VB.TextBox T_EP1 
         Height          =   270
         Left            =   480
         TabIndex        =   17
         Text            =   "EP'"
         Top             =   1920
         Width           =   2415
      End
      Begin VB.TextBox Text2 
         Height          =   270
         Left            =   1560
         TabIndex        =   13
         Text            =   "Text6"
         Top             =   240
         Width           =   375
      End
      Begin VB.TextBox Text1 
         Height          =   270
         Left            =   1080
         TabIndex        =   11
         Text            =   "Text5"
         Top             =   240
         Width           =   375
      End
      Begin VB.TextBox T_AP1 
         Height          =   270
         Left            =   480
         TabIndex        =   9
         Text            =   "AP'"
         Top             =   1680
         Width           =   2415
      End
      Begin VB.TextBox T_EP 
         Height          =   270
         Left            =   480
         TabIndex        =   5
         Text            =   "EP"
         Top             =   1080
         Width           =   2415
      End
      Begin VB.TextBox T_AP 
         Height          =   270
         Left            =   480
         TabIndex        =   1
         Text            =   "AP"
         Top             =   840
         Width           =   2415
      End
      Begin VB.Label Label16 
         Caption         =   "目标轨道/当前轨道"
         Height          =   375
         Left            =   2040
         TabIndex        =   40
         Top             =   240
         Width           =   1575
      End
      Begin VB.Label Unit 
         Caption         =   "(m)"
         Height          =   255
         Index           =   4
         Left            =   2880
         TabIndex        =   16
         Top             =   1920
         Width           =   495
      End
      Begin VB.Label Unit 
         Caption         =   "(m)"
         Height          =   255
         Index           =   3
         Left            =   2880
         TabIndex        =   15
         Top             =   1680
         Width           =   495
      End
      Begin VB.Label Unit 
         Caption         =   "(m)"
         Height          =   255
         Index           =   2
         Left            =   2880
         TabIndex        =   14
         Top             =   1080
         Width           =   495
      End
      Begin VB.Line Line1 
         X1              =   1560
         X2              =   1440
         Y1              =   240
         Y2              =   480
      End
      Begin VB.Label Unit 
         Caption         =   "(m)"
         Height          =   255
         Index           =   1
         Left            =   2880
         TabIndex        =   12
         Top             =   840
         Width           =   495
      End
      Begin VB.Label Label10 
         Caption         =   "共振系数K"
         Height          =   255
         Left            =   120
         TabIndex        =   10
         Top             =   240
         Width           =   1095
      End
      Begin VB.Label Label7 
         Caption         =   "Ep >"
         ForeColor       =   &H000080FF&
         Height          =   255
         Left            =   120
         TabIndex        =   8
         Top             =   1920
         Width           =   2655
      End
      Begin VB.Label Label6 
         Caption         =   "Ap >"
         ForeColor       =   &H000080FF&
         Height          =   255
         Left            =   120
         TabIndex        =   7
         Top             =   1680
         Width           =   2655
      End
      Begin VB.Label Label5 
         Caption         =   "目标轨道 >"
         ForeColor       =   &H00000000&
         Height          =   255
         Left            =   120
         TabIndex        =   6
         Top             =   1440
         Width           =   1575
      End
      Begin VB.Label Label4 
         Caption         =   "Ep"
         Height          =   255
         Left            =   120
         TabIndex        =   4
         Top             =   1080
         Width           =   615
      End
      Begin VB.Label Label3 
         Caption         =   "Ap"
         Height          =   255
         Left            =   120
         TabIndex        =   3
         Top             =   840
         Width           =   615
      End
      Begin VB.Label Label2 
         Caption         =   "当前轨道"
         ForeColor       =   &H00000000&
         Height          =   255
         Left            =   120
         TabIndex        =   2
         Top             =   600
         Width           =   2175
      End
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Dim AP0 As Single, EP0 As Single, AP1 As Single, EP1 As Single, K As Single, R As Single
Dim GM As Single
Const pi = 3.14159265359
Function QC(number As Single, inverse_of_precision As Single) As String '四舍五入到精确位数
QC = CStr(Int(number * inverse_of_precision + 0.5) / inverse_of_precision)
End Function
Function TNC(T_text As String) As Single '提取并合并字符串中的数字
Dim ch As String
    For i = 1 To Len(T_text)
        ch = Mid(T_text, i, 1)
        If "0" <= ch And ch <= "9" Then
            TNC = TNC * 10 + Val(ch)
        End If
    Next i
End Function
Function NTC(num As Single) As String '数字转换为字符串(带逗号)
Dim i As Integer
    i = 0
    Do While num > 0
        If i = 3 Then
            NTC = "," & NTC
            i = 0
        Else
            NTC = (num Mod 10) & NTC
            num = num \ 10
            i = i + 1
        End If
    Loop
End Function
Function TTC(txt As String) As String '文字转换为字符串(带逗号)
Dim i As Integer, L As Integer
Dim a(10) As String, s As String
    L = Len(txt)
    i = 0
    Do While L - 2 - 3 * i > 0
        a(i) = Mid(txt, L - 2 - 3 * i, 3)
        i = i + 1
    Loop
    a(i) = Mid(txt, 1, L - 3 * i)
    If a(i) <> "" Then
        TTC = a(i): i = i - 1
    Else
        TTC = a(i - 1): i = i - 2
    End If
    Do While i >= 0
        TTC = TTC & "," & a(i)
        i = i - 1
    Loop
End Function
'初始化--------------------------------------------------------------------
Private Sub Form_Load()
Text1.Text = "": Text2.Text = "": Text3.Text = "": Text4.Text = "": Text5.Text = ""
Text6.Text = "3.532": Text7.Text = "12": Text8.Text = "": Text9.Text = "": Text10.Text = ""
Text11.Text = ""
R_R.Text = "600"
T_AP.Text = ""
T_AP1.Text = ""
T_EP.Text = ""
T_EP1.Text = ""
End Sub
'**************************************************************************
'Model-1:共振轨道数据计算--------------------------------------------------
Function XP_C(AP0, EP0, YP, K, R) As Single '计算目标共振轨道的端点(AP/EP)
    XP_C = (AP0 + EP0 + 2 * R) * K ^ (2 / 3) - 2 * R - YP
End Function
Private Sub Label6_Click()
AP0 = TNC(T_AP.Text): EP0 = TNC(T_EP.Text): EP1 = TNC(T_EP1.Text)
R = Val(R_R.Text) * 1000
K = Val(Text1.Text) / Val(Text2.Text)
AP1 = XP_C(AP0, EP0, EP1, K, R)
T_AP1 = NTC(Int(AP1 + 0.5))
End Sub
Private Sub Label7_Click()
AP0 = TNC(T_AP.Text): EP0 = TNC(T_EP.Text): AP1 = TNC(T_AP1.Text)
R = NTC(R_R.Text) * 1000
K = Val(Text1.Text) / Val(Text2.Text)
EP1 = XP_C(AP0, EP0, AP1, K, R)
T_EP1 = CStr(Int(EP1 + 0.5))
T_EP1 = TTC(T_EP1)
End Sub
'**************************************************************************
'Model-2:轨道周期计算------------------------------------------------------
Function T_C(AP, EP, R) As Single '计算当前轨道周期
    a = (AP + EP + 2 * R) / 2
    T_C = 2 * pi * Sqr(a ^ 3 / (GM))
End Function
Private Sub Label13_Click()
Dim T As Single
Dim s As String
AP0 = TNC(Text3.Text): EP0 = TNC(Text4.Text)
R = NTC(R_R.Text) * 1000
GM = Val(Text6.Text) * 10 ^ Val(Text7.Text)
T = T_C(AP0, EP0, R)
Text5.Text = QC(T, 1000) 'CStr(Int(T * 1000 + 0.5) / 1000)
Text8.Text = CStr(T \ 3600) & "时" & CStr(T \ 60 Mod 60) & "分" & CStr(T Mod 60) & "秒"  '将时间处理为时分秒
End Sub
'**************************************************************************
'Model-3:轨道ap，ep参数计算
Function T_YP(XP, T, R) As Single '计算目标周期轨道的端点(AP/EP)
    a = (GM * T ^ 2 / (4 * pi ^ 2)) ^ (1 / 3)
    T_YP = 2 * (a - R) - XP
End Function
Private Sub Label18_Click() '计算ap参数
Dim T As Single
Dim s As String
EP0 = TNC(Text11.Text)
R = TNC(R_R.Text) * 1000
GM = Val(Text6.Text) * 10 ^ Val(Text7.Text)
T = Val(Text9.Text)
AP1 = T_YP(EP0, T, R)
Text10.Text = TTC(QC(AP1, 1)) 'CStr(Int(AP1 + 0.5))
End Sub
Private Sub Label19_Click() '计算ep参数
Dim T As Single
Dim s As String
AP0 = TNC(Text10.Text)
R = TNC(R_R.Text) * 1000
GM = Val(Text6.Text) * 10 ^ Val(Text7.Text)
T = Val(Text9.Text)
EP1 = T_YP(AP0, T, R)
Text10.Text = TTC(QC(EP1, 1))
End Sub
'**************************************************************************
