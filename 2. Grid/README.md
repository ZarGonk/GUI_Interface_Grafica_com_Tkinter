# GUI with Tkinter - Grid Geometry Manager

Learn how to organize widgets using **rows** and **columns** in Tkinter. The **Grid** geometry manager allows you to position widgets in a structured layout within a window or frame.

---

## Grid Concepts

The **Grid** geometry manager arranges widgets in a **grid** composed of **rows** and **columns**. Each position in the grid is called a **cell**, which is the intersection of a row and a column.

### Rows and Columns

- Each row and column has an **index**.
  - The first row/column has index `0`
  - The second row/column has index `1`
  - And so on
- Indices **do not have to start at zero** and can have gaps.  
  Example: columns with indices `1, 2, 10, 11, 12` can be useful for adding widgets later.

![Example of a 4x3 grid](assets/Tkinter-grid-Grid-Geometry.png)

---

### Cells

- A **cell** is where you place a widget.
- Each cell can contain **only one widget at a time**.
- Placing two or more widgets in the same cell will make them **overlap**.

---

### Grid Layout Table (Visual Representation)

| Row Index | Column 0       | Column 1       | Column 2       |
|-----------|----------------|----------------|----------------|
| 0         | Widget A       | Widget B       | Widget C       |
| 1         | Widget D       | Widget E       | Widget F       |
| 2         | Widget G       | Widget H       | Widget I       |
| 3         | Widget J       | Widget K       | Widget L       |

> This table shows a grid with **4 rows and 3 columns**. Each cell can hold one widget.
