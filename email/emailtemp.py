def template_for_email():

    html = """<html>
<body style="width:100%; margin:0; padding:0; background-color:#DED9D2;">
    <div style="text-align: center;">
    <table cellpadding="0" cellspacing="0" border="0" style="height:auto; margin:40px 0; padding:0; width:100%; background-color:#DED9D2; color:#222222;" align="center">
        <tr>
            <td>
             <div id="tablewrap" style="width:100%; max-width:600px; margin-top:0; margin-right: auto; margin-bottom:0; margin-left: auto;">
                  <table id="contenttable" width="600" cellpadding="0" cellspacing="0" border="0" style="background-color:#FFFFFF; margin-top:0; margin-right: auto; margin-bottom:0; margin-left: auto; border:none; width: 100%; max-width:600px;" align="center">
                    <tr>
                    <td width="100%">
                        <table bgcolor="#FFFFFF" border="0" cellspacing="0" cellpadding="0" width="100%" style="border-bottom: 2px solid rgb(244,121,32);padding: 10px;" align="center">
                            <tr style="text-align: center;" >
                                <td  bgcolor="#ffffff"><a href="#"><img src="otlogo.png" alt="" style="display:inline-block; width:80px; height:auto;border-bottom-right-radius:8px;border-bottom-left-radius:8px;" border="0"></a></td>
                                <td >
                                   <p style="font-size: 20px;color: #4c4c4c;font-family: sans-serif;"> Техникийн үг хэллэгийн хураангуй толь</p>
                                </td>
                            </tr>
                       </table>
                       <table bgcolor="#FFFFFF" border="0" cellspacing="0" cellpadding="25" width="100%" align="center">
                            <tr>
                                <td width="100%" bgcolor="#ffffff" style="text-align:center;">
                                    <p style="color:#4c4c4c; font-family: sans-serif; font-size:15px; line-height:19px; margin-top:0; margin-bottom:20px; padding:0; font-weight:normal;">
                                        Another day, another word!          
                                    </p>
                                   
                                        <table border="0" cellspacing="0" cellpadding="25" width="100%" style="border: 1px solid rgb(0,123,133);" >
                                          <tr>
                                            <td class="emailcolsplit" align="left" width="100%" style="background-color: rgb(0,123,133);" >
                                                <p style="color:#fff; font-family: sans-serif; font-size:20px; line-height:20px; margin-top:0; margin-bottom:20px; padding-top:20px; padding-left: 10px; font-weight:700;font-style: italic;">
                                                     {term_en}
                                                </p>
                                            </td>
                                          </tr>
                                          <tr>
                                            <td class="emailcolsplit" align="left" valign="top" width="100%" style="border-bottom: 1px solid rgb(0,123,133);">
                                                <p style="color:#4c4c4c; font-family: sans-serif; font-size:18px; line-height:20px; margin-top:0; margin-bottom:20px; padding-top:20px; padding-left: 10px; font-weight:700;font-style: italic;">
                                                     {}
                                                </p>
                                            
                                            </td>
                                          </tr>
                                          <tr>
                                            <td class="emailcolsplit" align="left" valign="top" width="100%">
                                                <p style="color:#4c4c4c; font-family: sans-serif; font-size:16px; line-height:20px; margin-top:0; margin-bottom:20px; padding-top:20px; padding-left: 10px; font-weight:normal;font-style: italic;">
                                                    Ашигтайгаар баяжуулж болох эрдэсжүүлэлтийн тооцоолсон агуулга ба 
                                                    жингийн тоо хэмжээ. Найдвартай байдлын зэрэглэлийн дагуу боломжит,
                                                    батлагдсан байдлаар нь ангилалд оруулж болно
                                                </p>
                                        
                                            </td>
                                          </tr>
                                        </table>
                                </td>
                            </tr>
                       </table>
                       <table bgcolor="#FFFFFF" border="0" cellspacing="0" cellpadding="25" width="100%">
                        <tr>
                            <td width="100%" bgcolor="#ffffff" style="text-align:center;">                               
                                    <table border="0" cellspacing="0" cellpadding="0" width="100%" class="emailwrapto100pc" style="border: 1px solid rgb(0,123,133);" >
                                      <tr>
                                        <td class="emailcolsplit" align="left" width="100%" style="background-color: rgb(0,123,133);" >
                                            <p style="color:#fff; font-family: sans-serif; font-size:20px; line-height:20px; margin-top:0; margin-bottom:20px; padding-top:20px; padding-left: 10px; font-weight:700;font-style: italic;">
                                                Block caving
                                            </p>
                                        </td>
                                      </tr>
                                      <tr>
                                        <td class="emailcolsplit" align="left" valign="top" width="100%" style="border-bottom: 1px solid rgb(0,123,133);">
                                            <p style="color:#4c4c4c; font-family: sans-serif; font-size:18px; line-height:20px; margin-top:0; margin-bottom:20px; padding-top:20px; padding-left: 10px; font-weight:700;font-style: italic;">
                                                Блокчлон олборлох, бөөн цөмрөг
                                            </p>
                                        
                                        </td>
                                      </tr>
                                      <tr>
                                        <td class="emailcolsplit" align="left" valign="top" width="100%">
                                            <p style="color:#4c4c4c; font-family: sans-serif; font-size:16px; line-height:20px; margin-top:0; margin-bottom:20px; padding-top:20px; padding-left: 10px; font-weight:normal;font-style: italic;">
                                                Маш том хэмжээний хүдрийг өндрөөс олборлон унагахад өөрийн жингээрээ цохигдоод 
                                                бутардаг олборлолтын хямд төсөр нэгэн арга. Гүний уурхайд илүү өргөн хэрэглэнэ
                                            </p>
                                    
                                        </td>
                                      </tr>
                                    </table>
                            </td>
                        </tr>
                   </table>
                       <table bgcolor="#FFFFFF" border="0" cellspacing="0" cellpadding="0" width="100%">
                            <tr style="text-align: center;">
                              <td width="100%" bgcolor="#ffffff" style="text-align:center;">
                                <a style="font-weight:bold; text-decoration:none;" href="#">
                                    <div style="display:inline-block; max-width:40%; width:100%; height:auto;background-color:#f47920;padding-top:15px;padding-right:15px;padding-bottom:15px;padding-left:15px;border-radius:8px;color:#ffffff;font-size:24px;font-family: sans-serif;">More words here!</div>
                                </a>
                            </td>
                            </tr>
                       </table>
                       <table bgcolor="#FFFFFF" border="0" cellspacing="0" cellpadding="25" width="100%">
                            <tr>
                                <td width="100%" bgcolor="#ffffff" style="text-align:left;">
                                    <p style="color:#222222; font-family: sans-serif; font-size:11px; line-height:14px; margin-top:0; margin-bottom:15px; padding:0; font-weight:normal;">
                                        Email not displaying correctly? <a style="color:#2489B3; font-weight:bold; text-decoration:underline;" href="#">View it in your browser.</a>
                                    </p>
                                    <p style="color:#222222; font-family: sans-serif; font-size:11px; line-height:14px; margin-top:0; margin-bottom:15px; padding:0; font-weight:normal;">
                                        OT Technical glossary<br>
                                        If you no longer wish to receive emails from us, you may <a style="color:#2489B3; font-weight:normal; text-decoration:underline;" href="#">unsubscribe</a>.
                                    </p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
            </div>
         </td>
        </tr>
    </table> 
</div>
    </body>
</html>"""