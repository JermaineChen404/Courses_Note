# VBA Vehicle Rental Cost Calculator

  

Files included:

- `VehicleRentalCalculator_Module.bas` -> paste/import into a **standard module**

- `ThisWorkbook_Code.txt` -> paste into **ThisWorkbook**

- `Rentals_Worksheet_Code.txt` -> paste into the **Rentals worksheet code window**

  

## Where each part goes

  

### 1) Standard module

Open the VBA editor with `Alt + F11`.

Then go to **Insert > Module** and paste the contents of `VehicleRentalCalculator_Module.bas`.

  

### 2) ThisWorkbook

In the Project Explorer, double-click **ThisWorkbook**.

Paste the contents of `ThisWorkbook_Code.txt` there.

  

### 3) Rentals sheet event

In the Project Explorer, double-click the **Rentals** sheet.

Paste the contents of `Rentals_Worksheet_Code.txt` there.

  

## Setup steps

1. Save the file as **Vehicle_Rentals.xlsm**.

2. Make sure the worksheet names are exactly:

   - `Rentals`

   - `Cover Page`

3. Make sure cell `I19` is named `TotalRevenue`.

4. Run `SetupInterfaceButtons` once to create:

   - Run Calculator

   - Reset Data

5. Run `SetupNavigationButtons` once if you want navigation buttons for the cover page visibility requirement.

  

## Expected behavior

- `CalculateRentals` calculates each row total in column I.

- `ResetData` clears `I7:I16` and `TotalRevenue` after confirmation.

- `Workbook_Open` shows only the Cover Page.

- `Worksheet_SelectionChange` auto-fits columns C:K on the Rentals sheet.

  

## Quick validation target

Using the uploaded CSV values, the grand total should come out to **$3,801.10** after calculation.