/**
 * Created with PyCharm.
 * User: milu
 * Date: 10/8/14
 * Time: 6:03 PM
 * To change this template use File | Settings | File Templates.
 */


var s = document.createElement('script');
s.type = 'text/javascript';
s.src = 'http://127.0.0.1:8000/static/js/jquery.min.js';
document.getElementsByTagName('head')[0].appendChild(s) && 0;

 $.ajax({

                        url : "http://127.0.0.1:8000/",
                        type: "POST",
                        data : {
                                "patient_id":"1"
                        },
                        success: function(data, textStatus, jqXHR)
                        {
                            console.log(data);

                        },
                        error: function (jqXHR, textStatus, errorThrown)
                        {

                        }
                    });