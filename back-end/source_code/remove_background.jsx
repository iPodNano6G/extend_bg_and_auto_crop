
            var idOpn = charIDToTypeID( "Opn " );
                var desc349 = new ActionDescriptor();
                var iddontRecord = stringIDToTypeID( "dontRecord" );
                desc349.putBoolean( iddontRecord, false );
                var idforceNotify = stringIDToTypeID( "forceNotify" );
                desc349.putBoolean( idforceNotify, true );
                var idnull = charIDToTypeID( "null" );
                desc349.putPath( idnull, new File( "C:\\SDP\\automated_image_processing\\back-end\\source_code\\image_data\\ssfshop\\beanpole\\³²³à°ø¿ë º£ÀÌÁ÷ ÇÇÄÉ Æ¼¼ÅÃ÷ - ºí·¢\\original.jpg" ) );
                var idDocI = charIDToTypeID( "DocI" );
                desc349.putInteger( idDocI, 72 );
                var idtemplate = stringIDToTypeID( "template" );
                desc349.putBoolean( idtemplate, false );
            executeAction( idOpn, desc349, DialogModes.NO );

            // ======================

            var idsetd = charIDToTypeID( "setd" );
                var desc326 = new ActionDescriptor();
                var idnull = charIDToTypeID( "null" );
                    var ref15 = new ActionReference();
                    var idLyr = charIDToTypeID( "Lyr " );
                    var idBckg = charIDToTypeID( "Bckg" );
                    ref15.putProperty( idLyr, idBckg );
                desc326.putReference( idnull, ref15 );
                var idT = charIDToTypeID( "T   " );
                    var desc327 = new ActionDescriptor();
                    var idOpct = charIDToTypeID( "Opct" );
                    var idPrc = charIDToTypeID( "#Prc" );
                    desc327.putUnitDouble( idOpct, idPrc, 100.000000 );
                    var idMd = charIDToTypeID( "Md  " );
                    var idBlnM = charIDToTypeID( "BlnM" );
                    var idNrml = charIDToTypeID( "Nrml" );
                    desc327.putEnumerated( idMd, idBlnM, idNrml );
                var idLyr = charIDToTypeID( "Lyr " );
                desc326.putObject( idT, idLyr, desc327 );
                var idLyrI = charIDToTypeID( "LyrI" );
                desc326.putInteger( idLyrI, 5 );
            executeAction( idsetd, desc326, DialogModes.NO );


            // ===================================================

            var idremoveBackground = stringIDToTypeID( "removeBackground" );
            executeAction( idremoveBackground, undefined, DialogModes.NO );


            // =======================================================
            var idsave = charIDToTypeID( "save" );
                var desc255 = new ActionDescriptor();
                var idAs = charIDToTypeID( "As  " );
                    var desc256 = new ActionDescriptor();
                    var idMthd = charIDToTypeID( "Mthd" );
                    var idPNGMethod = stringIDToTypeID( "PNGMethod" );
                    var idquick = stringIDToTypeID( "quick" );
                    desc256.putEnumerated( idMthd, idPNGMethod, idquick );
                    var idPGIT = charIDToTypeID( "PGIT" );
                    var idPGIT = charIDToTypeID( "PGIT" );
                    var idPGIN = charIDToTypeID( "PGIN" );
                    desc256.putEnumerated( idPGIT, idPGIT, idPGIN );
                    var idPNGf = charIDToTypeID( "PNGf" );
                    var idPNGf = charIDToTypeID( "PNGf" );
                    var idPGAd = charIDToTypeID( "PGAd" );
                    desc256.putEnumerated( idPNGf, idPNGf, idPGAd );
                    var idCmpr = charIDToTypeID( "Cmpr" );
                    desc256.putInteger( idCmpr, 6 );
                    var idembedIccProfileLastState = stringIDToTypeID( "embedIccProfileLastState" );
                    var idembedOff = stringIDToTypeID( "embedOff" );
                    var idembedOff = stringIDToTypeID( "embedOff" );
                    desc256.putEnumerated( idembedIccProfileLastState, idembedOff, idembedOff );
                var idPNGF = charIDToTypeID( "PNGF" );
                desc255.putObject( idAs, idPNGF, desc256 );
                var idIn = charIDToTypeID( "In  " );
                desc255.putPath( idIn, new File( "C:\\SDP\\automated_image_processing\\back-end\\source_code\\image_data\\ssfshop\\beanpole\\³²³à°ø¿ë º£ÀÌÁ÷ ÇÇÄÉ Æ¼¼ÅÃ÷ - ºí·¢\\no_background.png" ) );
                var idDocI = charIDToTypeID( "DocI" );
                desc255.putInteger( idDocI, 59 );
                var idLwCs = charIDToTypeID( "LwCs" );
                desc255.putBoolean( idLwCs, true );
                var idEmbP = charIDToTypeID( "EmbP" );
                desc255.putBoolean( idEmbP, false );
                var idsaveStage = stringIDToTypeID( "saveStage" );
                var idsaveStageType = stringIDToTypeID( "saveStageType" );
                var idsaveSucceeded = stringIDToTypeID( "saveSucceeded" );
                desc255.putEnumerated( idsaveStage, idsaveStageType, idsaveSucceeded );
            executeAction( idsave, desc255, DialogModes.NO );

            // =======================================================
            var idCls = charIDToTypeID( "Cls " );
                var desc322 = new ActionDescriptor();
                var idSvng = charIDToTypeID( "Svng" );
                var idYsN = charIDToTypeID( "YsN " );
                var idN = charIDToTypeID( "N   " );
                desc322.putEnumerated( idSvng, idYsN, idN );
                var idDocI = charIDToTypeID( "DocI" );
                desc322.putInteger( idDocI, 88 );
                var idforceNotify = stringIDToTypeID( "forceNotify" );
                desc322.putBoolean( idforceNotify, true );
            executeAction( idCls, desc322, DialogModes.NO );
        