<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>

<h1 style="text-align:center; color:#8B0000"> UTRGV B.S Computer Science </h1>
<h2 style="text-align:center; color:#8B0000"> Class Planning Worsheet </h2>

<xsl:for-each select="advising/studentinfo">
    <p style="text-align:left;"> <span style="color:#8B0000;">Student Name: </span> <xsl:value-of select="f_name"/>&#160;<xsl:value-of select="l_name"/></p>
    <p style ="text-align:left;"> <span style="color:#8B0000;">Student ID: </span> <xsl:value-of select="student_id"/></p>
    <p style ="text-align:left;"> <span style="color:#8B0000;">Student Advisor: </span> <xsl:value-of select="faculty_advisor"/></p>
    <p style ="text-align:left;"> <span style="color:#8B0000;">Date: </span> <xsl:value-of select="adv_date"/></p>
</xsl:for-each>    

<body>
 <h2 style="text-align:center;color:red">
<xsl:value-of select="advising/semester[1]/name"/>&#160;
<xsl:value-of select="advising/semester[1]/year"/>
</h2>

  <table style="width:100%"> 
     <tr>
        <th  style="text-align: left;padding: 5px; background-color:orange;"> Prefix 
        </th>
        <th style="text-align: left;padding: 5px; background-color:orange;"> Name 
        </th>
        <th style="text-align: left;padding: 5px; background-color:orange;"> Hours 
        </th>
      </tr>
  <xsl:for-each select="advising/semester[1]/course">
     <tr>
        <td> <xsl:value-of select="number"/> </td> 
        <td><xsl:value-of select="section"/> </td> 
        <td><xsl:value-of select="hours"/> </td>
     </tr>
  </xsl:for-each>
 </table>

<h2 style="text-align:center;color:red">
<xsl:value-of select="advising/semester[2]/name"/>&#160;
<xsl:value-of select="advising/semester[2]/year"/>
</h2>


<table style="width:100%"> 
     <tr>
        <th  style="text-align: left;padding: 5px; background-color:orange;"> Prefix 
        </th>
        <th style="text-align: left;padding: 5px; background-color:orange;"> Name 
        </th>
        <th style="text-align: left;padding: 5px; background-color:orange;"> Hours 
        </th>
      </tr>
  <xsl:for-each select="advising/semester[2]/course">
     <tr>
        <td> <xsl:value-of select="number"/> </td> 
        <td><xsl:value-of select="section"/> </td> 
        <td><xsl:value-of select="hours"/> </td>
     </tr>
  </xsl:for-each>
 </table>


<h2 style="text-align:center;color:red">
<xsl:value-of select="advising/semester[3]/name"/>&#160;
<xsl:value-of select="advising/semester[3]/year"/>
</h2>


<table style="width:100%"> 
     <tr>
        <th  style="text-align: left;padding: 5px; background-color:orange;"> Prefix 
        </th>
        <th style="text-align: left;padding: 5px; background-color:orange;"> Name 
        </th>
        <th style="text-align: left;padding: 5px; background-color:orange;"> Hours 
        </th>
      </tr>
  <xsl:for-each select="advising/semester[3]/course">
     <tr>
        <td> <xsl:value-of select="number"/> </td> 
        <td><xsl:value-of select="section"/> </td> 
        <td><xsl:value-of select="hours"/> </td>
     </tr>
  </xsl:for-each>
 </table>

  <p style="text-align:left;"> Notes: <span style="color:#8B0000;"> <xsl:value-of select="advising/notes"/> </span> </p>

</body>
</html>
</xsl:template>
</xsl:stylesheet>

