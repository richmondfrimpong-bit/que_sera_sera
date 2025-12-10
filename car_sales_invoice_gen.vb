'Group Members              ===> Index no.
'Adu-Sefa Yaa Konadu        ===> 8688121
'Aboagye Kodua Bright       ===> 8687721
'Aboagye Richmond Frimpong  ===> 8687621
Public Class Form1
'Car_choice() is Function Procedure to return the price of the brand
'of car chosen
Private Function Car_choice()
Dim choice As Double
If Toyota_Camry.Checked Then
choice = 30000
ElseIf Volkswagen.Checked Then
choice = 39420
ElseIf Lexus_LX.Checked Then
choice = 93915
ElseIf Honda.Checked Then
choice = 32545
ElseIf Mercedes_C300.Checked Then
choice = 41600
ElseIf Chevrolet.Checked Then
choice = 49890
End If
Return choice
End Function
'exterior() is a function procedure which returns the prices
'associated with the exterior
'design of the car
Private Function exterior()
Dim exte As Double
If Standard.Checked Then
exte = 0
ElseIf Pearlized.Checked Then
exte = 543.27
ElseIf Customized.Checked Then
exte = 698.74
End If
Return exte
End Function
'accessories() is a function procedure which returns the prices
'associated with
'some of the interior designs of the car like the stereo and Co.
Private Function accessories()
Dim access As Double
If Stereo.Checked Then
access = 524.67
ElseIf Leather.Checked Then
access = 789.14
ElseIf Computer_Nav.Checked Then
access = 3471.32
End If
Return access
End Function
'Accumulator() is a function proceture which returns the subtotal of
'the sales
'before the inclusion of tax
Private Function Accumulator()
Dim accumulate
Dim carchoice As Double = Car_choice()
Dim Exter As Double = exterior()
Dim Accexx As Double = accessories()
accumulate = carchoice + Exter + Accexx
Return accumulate
End Function
'Next_Clear() is a sub procedure which executes to uncheck and clear
'all radio,checkboxes
''and textboxes except the Car_Count and TotCar_Sales textboxes
Private Sub Next_clear()
Toyota_Camry.Checked = False
Volkswagen.Checked = False
Lexus_LX.Checked = False
Honda.Checked = False
Mercedes_C300.Checked = False
Chevrolet.Checked = False
Standard.Checked = False
Pearlized.Checked = False
Customized.Checked = False
Stereo.Checked = False
Leather.Checked = False
Computer_Nav.Checked = False
SubTot.Clear()
Total.Clear()
Trade_in_allowance.Clear()
Amt_due.Clear()
End Sub
'Totals() is a function procedure which returns the value of the
'Amt_due textbox and also
'set the value of the SubTot and Total textboxes
Private Function Totals()
Dim calc As Double = Accumulator()
Dim tax As Double
Dim trade As Double
Dim amount As Double
Dim inttot As Double
tax = calc * 0.08
inttot = calc + tax
Total.Text = inttot
trade = Val(Trade_in_allowance.Text)
amount = inttot -trade
SubTot.Text = calc
Amt_due.Text = amount
Return amount
End Function
'somecounting() is a function procedure that returns the counter value
'of 1
Private Function somecounting()
Dim count As Integer
count = 1
Return count
End Function
'Tsales() is a function procedure that returns the individual total
'sales at a time
Private Function Tsales()
Dim addup As Double = Totals()
Dim addmeup As Double
addmeup = addmeup + addup
Return addmeup
End Function
'DispT() is a sub procedure that executes to perform the counting of
'the number of cars
'sold in a day and also do the summing for the total sales in a day
Private Sub DispT()
TotCar_Sales.Text = Val(TotCar_Sales.Text) + Tsales()
Car_Count.Text = Val(Car_Count.Text) + somecounting()
End Sub
' Confirmation() is a sub procedure that executes to display a message
'box
' containing a summary of the sales made at a time
Private Sub Confirmation()
Dim messg
Dim Response
messg = "=====Confirm Sales=====".ToUpper & vbNewLine & vbNewLine
messg = messg + "Subtotal = Ghc " & Accumulator() & vbNewLine &vbNewLine
messg = messg + "Sales tax(8%) = Ghc " & Accumulator() * 0.08 &vbNewLine & vbNewLine
messg = messg + "Total = Ghc " & Accumulator() + Accumulator() * 0.08 & vbNewLine & vbNewLine
messg = messg + "Trade-in-discount = Ghc " & Trade_in_allowance.Text & vbNewLine & vbNewLine
messg = messg + "Total amount due = Ghc " & Totals()
Response = MsgBox(messg, vbOKCancel, "Sales Summary")
If Response = vbCancel Then
Next_clear()
End If
End Sub

Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
End Sub
'The sub procedure below is an event procedure which executes when the
''(Next button) on the
'form is clicked
Private Sub Button4_Click(sender As Object, e As EventArgs) Handles NextSales.Click
DispT()
Next_clear()
somecounting()
End Sub
'The event procedure below executes when the (Enter button) on the
form is clicked.
Private Sub Button3_Click(sender As Object, e As EventArgs) Handles Calc_Sales.Click
Confirmation()
Totals()
End Sub
'The event procedure below handles the "Clear" button on the form and
'resets the form
'when clicked.
'It unchecks all radiobuttons and checkboxes and empties all textboxes
Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Clear_Set.Click
Next_clear()
TotCar_Sales.Clear()
Car_Count.Clear()
End Sub
'The event procedure below handles the "Exit" button on the form and
'closes the form when
'clicked.
Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Exit_prog.Click
Me.Close()
End Sub
End Class