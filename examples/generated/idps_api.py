"""
Examples for using the IdpsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import IdpsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = IdpsApi(api_client)

def example_create_idp():
    """
    Example of using create_idp
    
    Configure external idp
    
    """
    try:
        # Prepare the request parameters
        
        # Create example data for IdpCreationRequest
        idp_creation_request = models.IdpCreationRequest(
            name = '',
            type = 'oidc',
            saml_data = runai.models.saml_creation_data.SamlCreationData(
                    metadata_xml_url = '', 
                    metadata_xml_file = '', 
                    file_name = '', 
                    metadata_xml_type = null, 
                    entity_id = '', ),
            oidc_data = runai.models.oidc_creation_data.OidcCreationData(
                    client_id = '0', 
                    client_secret = '0', 
                    discover_document_url = '', 
                    scopes = [
                        '0 JLe6iL71-aa-.Ctq:dcsc.3-8:1g 8Xa6u61ArrlGpCQjkQVRmfnjddwcDM.:fvlxVU:5mAsDwtJsoLm0U2Qzc bMGoFtYYnOi3Uynm7-iBPXDeXK7FerdNFRGYVtmAOl5_Cq2Rl4hC2QiYJ5AOF77DBqQaK90sLp4g4V9O-6o daJrr3kIA8m85_YUSTN-PJy8dgSQzlarQkEaQ7MSI_JXg0j7ljZfgn2bLVk .jh-SQfnnBmLmok4-qyj::FnMc c1s:zY.5cKhAX0a5bAbk48VRGGhVIVFbPoXoEqb1EjLwWHMEWwnY_Z2TcNg1eoeI:Sh..EKMforDc7IjMfFpU0 0osd6el-_scVo4.4LpdT7v:MWCKJ--bQ2llJ.xnhemZK2YEVOdfGqWVRaJTQ6NZjv7Fim84dl:6u:bf 1siac5xO36MmDLWjJ3jQlUx0EM7QTdbqkuy39oC5lk0tnyKSHbk-zevT:KaSOnxfj6h3vQb5v8wk6Sg8 5NDiQoZsM.l6i6i:X3nW1dw8EowTNIWEw9A9emf4X1K3ldM15JuA8a:fOZ9xEnRJanu0Ocoq2B7wgBww9rSjSF 04JADnYUXiaAascLalMZXWxP.coV3uIqL2NwG1Q15bVN8-C4QbrRP8xA 4fth0O_ATmjWCKOzvZrmHsFgm1BjNZgMZgeBXCspwU7tvy Rc4xEuKdFMjyAKR9T_PAefg3k17A:4:LQ0hCGa qQO7invEoLeDe-T2FaL5:Eugu9mSRm1:hhMc_fyRqSs6qs6m:6:uapkGM.emZJKhxxu.cSv4lgZIy39ZAP 183DZ6eFRHoCI32RZpIF1hrunoV2CN8hBG3asQY9si01no:Lr29sCi5fusnO0Pt9m_WBzmDQ.rY-.dWc8IoIfsOVxrxONEet:y2Ea2WBnlIeVDDvoQkWfnHqpzl38HSun:67NTGpyvcLUvLesddb7ZeMnxTiEdp3QB25:xPgTL:jsXt6AS-qWtRiUTSPvdeYfIa5D9W:m3zlielNqY57V5GNavSBLiBzZEK-XN5w5vzvhhxxZvZ6DSZk7t.Yolw3zR W54JVAgX5uBCBgOEU-0z8IvupQn1Ln7KN9-Rm8grr3yUXv8ymTkuKbSl:ey-0o3kDV _NwFlRcRlkQG052yAruvGoDsRGUWvpp1g3iLwXxMqtsSg-S-mz4inAC2m16mBnktro i:E.Q97mOyiQ-PlkSWd2vgJF_wnac2TI0P3OQpfYVThWWtT9C4EMdkEGXvo_pF8a LrcWJySttXG_L_wVcihNkaQVvG2k6.uK19A8bsb5bHBstV_iIURKFgWngEotMsNwFg4m4G2eGYR8Mev:ehM20oC Errt5WLpKogarQ79jUuJvoXzAALsnC:L2n9:1NrppKZo51WAYJ-O2VKkDZikuODyWW0miNkaUbJIKSGQz_mnaoCLSQ_OtCiGx2GBiVurYQU0 tHCmwy3_ZeZA8sXIqyMK5hfbO8CdOVIQ4-HWt1xfvGn3nycbCcB7ppl1xtGm tRB-edDfMd3SIbhyKQMLYa0D8SK2ROcYS6s8bD.Hj9Vrukx9 IXyLnTz6BL189TiKs1hzAmdz_H34DxOE1dqyOEzw2z:UfO6ZOCxGJIaF45I6qCx7vRzlOA:WVc:KzPhB40gB1s-q LQ6wRNld4ksNBvgoQbDSWwAEMIc3Lj1ZgSMD0kq10azd CNZotNqQMCcju5aZsU-.FOOCz1M6jYtjmzvGJFn2fomOLL_hhqKOV60ej4Wnb_Apr4Ii_830jhIct4_rnneTA ..ovWFYW.CDaz46v9mCKpToacUmuGfCXEgzBnP79sSBiK5J6DY2iFdET cuwWm5l6xJxLA1YFRqNFkORfSvLyHt-wefW4HUCgpVF5n7APxkF8Nq1-YWQXnC5Y0ywM6ra0fyPpof3VJr49NnQIM51BNoxsmnTY1739rkUGdgd74tjas0TsDj5wyogLbwq-uTK1ZSfODxfI5QrkOFgTfOJGSbCqcPFMR3oslc:vpXnLorh5IU6uq.kNtRBhdJpSG1krkOL5MnFWE4P0-orkSE61hbFzxTbuQc._CwA_cp-f8GTTep6KCSJfW.E6Zdi tN_1o.-93XmBlm1HhlFW2zKw5vRQCs.l8MU30wJ0Xu4zaw6ZBCeyDXp.35yLDHME3VQ4V9g8G vZOdS5Dqbe0Oq4p-3JFwIM265vdxXSEblrXLwsD56B1sm2fZZ_bSdPjKZMNe-SiE7E CF9R6igWguK38C-YraMyWtjI3LzdIwl LOrclq3ZeaFeS_cB.PcTw2F4.Qy9f7.THaGxysoJ79-Jh7_hh0aY28FE-hKazu2q3ZSgSxP7:.9sjse8DuY00860KstM44-0TNAtJJMpMKh7thZ37KQ6Yz45:EAe:eM:5ByDb:UF-H08dH6ENnOyK0rn-.7nj2o9.I JjhiBor6nvE2Bma7t5_0T9S.k.PlpeHxBZj_nZnSqrt8Q_3PmUNmV6ElLRzt6qdGD -o4ENqGg4sU2clcshSIKL6f91oYknUPgy9SzJ5 2e7VcTJR5lRaJ6vbt-w_u3bRL.UYuVHga1BZs1cGujVpFQPgZawqkh6Ol7Rhf8zYz2Xeit5C8Q.81Ud:PwaA8KCYLzw681h rzxd8cpSQSbF1dYbIr23c0snlZjFHRpfWGrvYTpIIGO-_9prQk6F6xlc91-JWKZiEs93TaiRpcNLUKhtKvojBba_NwfiM0TmNCT_Wkp6hZLEFsEMb.I3l9c9z8u.c5oyGUNrHqlgyf.jcM:bkOP-tqJCvg I:bROCxOuQxLs7.UmGqoYnGmxwAVq2LPLBRjKM0pRLkDCBlF07zgqZcklnDNngwtOv:uSEFxM7zrskU3J_r71Q-.y5y9CSqJeGnyzs.vV0JSlLRfIqIYN34uhQpQF3PP1fjnhOr1nrPls5PcefAlsQBVYpZYj j28vlhigAJFKibS0F8kjuosVcKs5ZG:-D9F:92L9szPZ5gwrK6vwUqPfmW:ud_3F3KPFTlwx0K.ebAlFsyge0khhbbtQky2yND:FHpXJGrZDg4L-ocNz9VaQlP1aglh-FZUr55YNHq:2W j4eBDEmkb1qqTVohVN_Dbai2Y9:GvIitIehfcfMBzd.VfZRyMhl.0_oJ5qXd:0syO1bg2ZOdgkHncAMCg9fGsrVMyvqQPW1:6GtR8z1T7hDB1lNwHA:APHxC3CnVD:h0mztR8Ede_n8uuQ5QEd0.O60APIr045S3a1qyOCZORhPNuZQZUR8zEN_mU2ASTYnh0nT411-0q2zinWNpU3sfPF6d3i1uHRJu1ll6NxtpA2yX7fHQ kYJ0E5A2DP6EkHbyU6Vhy_cCMi.LQ7:yW.l2OPU9btfLxZay-AzzqWyVtoW:YDpEXdX3W1Qs7ExXxH6sgXc-B: sllDaUUdPbtWRpkAd327lBy30Vu8Ms9Gt.Vg5PyuLUXwlXx2-Kdl5o7cZmGK32rd0iJZduxLYd6I0NZhmQod7LeZOTLbSB1D1N-2q0NaV8.B4Z6YH2XxHb5INP2m:lK4:9UVwsYYkC:jCzRvoh FYL1 :0tF.6qtuVKEwSIfN2z52zDVxOyJK2UhLLVF1-EjuwmkUZ_lJQG32Al392JxPtH_IWdzEVTBbaU68dh_YVTqN-SYh263UL1kK xb9EvP8QzfbIXzsncvZ_3cFFflBDN5SlsWvgnHaPQ8lC94xmtsePqTu3fpMHEAPabvJF'
                        ], 
                    mandatory_claim = {values=[Ljava.lang.Object;@625487a6, claim=claim}, ),
            ocp_data = runai.models.ocp_creation_data.OcpCreationData(
                    client_id = '0', 
                    idp_base_url = '', 
                    client_secret = '0', 
                    scopes = [
                        '0 JLe6iL71-aa-.Ctq:dcsc.3-8:1g 8Xa6u61ArrlGpCQjkQVRmfnjddwcDM.:fvlxVU:5mAsDwtJsoLm0U2Qzc bMGoFtYYnOi3Uynm7-iBPXDeXK7FerdNFRGYVtmAOl5_Cq2Rl4hC2QiYJ5AOF77DBqQaK90sLp4g4V9O-6o daJrr3kIA8m85_YUSTN-PJy8dgSQzlarQkEaQ7MSI_JXg0j7ljZfgn2bLVk .jh-SQfnnBmLmok4-qyj::FnMc c1s:zY.5cKhAX0a5bAbk48VRGGhVIVFbPoXoEqb1EjLwWHMEWwnY_Z2TcNg1eoeI:Sh..EKMforDc7IjMfFpU0 0osd6el-_scVo4.4LpdT7v:MWCKJ--bQ2llJ.xnhemZK2YEVOdfGqWVRaJTQ6NZjv7Fim84dl:6u:bf 1siac5xO36MmDLWjJ3jQlUx0EM7QTdbqkuy39oC5lk0tnyKSHbk-zevT:KaSOnxfj6h3vQb5v8wk6Sg8 5NDiQoZsM.l6i6i:X3nW1dw8EowTNIWEw9A9emf4X1K3ldM15JuA8a:fOZ9xEnRJanu0Ocoq2B7wgBww9rSjSF 04JADnYUXiaAascLalMZXWxP.coV3uIqL2NwG1Q15bVN8-C4QbrRP8xA 4fth0O_ATmjWCKOzvZrmHsFgm1BjNZgMZgeBXCspwU7tvy Rc4xEuKdFMjyAKR9T_PAefg3k17A:4:LQ0hCGa qQO7invEoLeDe-T2FaL5:Eugu9mSRm1:hhMc_fyRqSs6qs6m:6:uapkGM.emZJKhxxu.cSv4lgZIy39ZAP 183DZ6eFRHoCI32RZpIF1hrunoV2CN8hBG3asQY9si01no:Lr29sCi5fusnO0Pt9m_WBzmDQ.rY-.dWc8IoIfsOVxrxONEet:y2Ea2WBnlIeVDDvoQkWfnHqpzl38HSun:67NTGpyvcLUvLesddb7ZeMnxTiEdp3QB25:xPgTL:jsXt6AS-qWtRiUTSPvdeYfIa5D9W:m3zlielNqY57V5GNavSBLiBzZEK-XN5w5vzvhhxxZvZ6DSZk7t.Yolw3zR W54JVAgX5uBCBgOEU-0z8IvupQn1Ln7KN9-Rm8grr3yUXv8ymTkuKbSl:ey-0o3kDV _NwFlRcRlkQG052yAruvGoDsRGUWvpp1g3iLwXxMqtsSg-S-mz4inAC2m16mBnktro i:E.Q97mOyiQ-PlkSWd2vgJF_wnac2TI0P3OQpfYVThWWtT9C4EMdkEGXvo_pF8a LrcWJySttXG_L_wVcihNkaQVvG2k6.uK19A8bsb5bHBstV_iIURKFgWngEotMsNwFg4m4G2eGYR8Mev:ehM20oC Errt5WLpKogarQ79jUuJvoXzAALsnC:L2n9:1NrppKZo51WAYJ-O2VKkDZikuODyWW0miNkaUbJIKSGQz_mnaoCLSQ_OtCiGx2GBiVurYQU0 tHCmwy3_ZeZA8sXIqyMK5hfbO8CdOVIQ4-HWt1xfvGn3nycbCcB7ppl1xtGm tRB-edDfMd3SIbhyKQMLYa0D8SK2ROcYS6s8bD.Hj9Vrukx9 IXyLnTz6BL189TiKs1hzAmdz_H34DxOE1dqyOEzw2z:UfO6ZOCxGJIaF45I6qCx7vRzlOA:WVc:KzPhB40gB1s-q LQ6wRNld4ksNBvgoQbDSWwAEMIc3Lj1ZgSMD0kq10azd CNZotNqQMCcju5aZsU-.FOOCz1M6jYtjmzvGJFn2fomOLL_hhqKOV60ej4Wnb_Apr4Ii_830jhIct4_rnneTA ..ovWFYW.CDaz46v9mCKpToacUmuGfCXEgzBnP79sSBiK5J6DY2iFdET cuwWm5l6xJxLA1YFRqNFkORfSvLyHt-wefW4HUCgpVF5n7APxkF8Nq1-YWQXnC5Y0ywM6ra0fyPpof3VJr49NnQIM51BNoxsmnTY1739rkUGdgd74tjas0TsDj5wyogLbwq-uTK1ZSfODxfI5QrkOFgTfOJGSbCqcPFMR3oslc:vpXnLorh5IU6uq.kNtRBhdJpSG1krkOL5MnFWE4P0-orkSE61hbFzxTbuQc._CwA_cp-f8GTTep6KCSJfW.E6Zdi tN_1o.-93XmBlm1HhlFW2zKw5vRQCs.l8MU30wJ0Xu4zaw6ZBCeyDXp.35yLDHME3VQ4V9g8G vZOdS5Dqbe0Oq4p-3JFwIM265vdxXSEblrXLwsD56B1sm2fZZ_bSdPjKZMNe-SiE7E CF9R6igWguK38C-YraMyWtjI3LzdIwl LOrclq3ZeaFeS_cB.PcTw2F4.Qy9f7.THaGxysoJ79-Jh7_hh0aY28FE-hKazu2q3ZSgSxP7:.9sjse8DuY00860KstM44-0TNAtJJMpMKh7thZ37KQ6Yz45:EAe:eM:5ByDb:UF-H08dH6ENnOyK0rn-.7nj2o9.I JjhiBor6nvE2Bma7t5_0T9S.k.PlpeHxBZj_nZnSqrt8Q_3PmUNmV6ElLRzt6qdGD -o4ENqGg4sU2clcshSIKL6f91oYknUPgy9SzJ5 2e7VcTJR5lRaJ6vbt-w_u3bRL.UYuVHga1BZs1cGujVpFQPgZawqkh6Ol7Rhf8zYz2Xeit5C8Q.81Ud:PwaA8KCYLzw681h rzxd8cpSQSbF1dYbIr23c0snlZjFHRpfWGrvYTpIIGO-_9prQk6F6xlc91-JWKZiEs93TaiRpcNLUKhtKvojBba_NwfiM0TmNCT_Wkp6hZLEFsEMb.I3l9c9z8u.c5oyGUNrHqlgyf.jcM:bkOP-tqJCvg I:bROCxOuQxLs7.UmGqoYnGmxwAVq2LPLBRjKM0pRLkDCBlF07zgqZcklnDNngwtOv:uSEFxM7zrskU3J_r71Q-.y5y9CSqJeGnyzs.vV0JSlLRfIqIYN34uhQpQF3PP1fjnhOr1nrPls5PcefAlsQBVYpZYj j28vlhigAJFKibS0F8kjuosVcKs5ZG:-D9F:92L9szPZ5gwrK6vwUqPfmW:ud_3F3KPFTlwx0K.ebAlFsyge0khhbbtQky2yND:FHpXJGrZDg4L-ocNz9VaQlP1aglh-FZUr55YNHq:2W j4eBDEmkb1qqTVohVN_Dbai2Y9:GvIitIehfcfMBzd.VfZRyMhl.0_oJ5qXd:0syO1bg2ZOdgkHncAMCg9fGsrVMyvqQPW1:6GtR8z1T7hDB1lNwHA:APHxC3CnVD:h0mztR8Ede_n8uuQ5QEd0.O60APIr045S3a1qyOCZORhPNuZQZUR8zEN_mU2ASTYnh0nT411-0q2zinWNpU3sfPF6d3i1uHRJu1ll6NxtpA2yX7fHQ kYJ0E5A2DP6EkHbyU6Vhy_cCMi.LQ7:yW.l2OPU9btfLxZay-AzzqWyVtoW:YDpEXdX3W1Qs7ExXxH6sgXc-B: sllDaUUdPbtWRpkAd327lBy30Vu8Ms9Gt.Vg5PyuLUXwlXx2-Kdl5o7cZmGK32rd0iJZduxLYd6I0NZhmQod7LeZOTLbSB1D1N-2q0NaV8.B4Z6YH2XxHb5INP2m:lK4:9UVwsYYkC:jCzRvoh FYL1 :0tF.6qtuVKEwSIfN2z52zDVxOyJK2UhLLVF1-EjuwmkUZ_lJQG32Al392JxPtH_IWdzEVTBbaU68dh_YVTqN-SYh263UL1kK xb9EvP8QzfbIXzsncvZ_3cFFflBDN5SlsWvgnHaPQ8lC94xmtsePqTu3fpMHEAPabvJF'
                        ], ),
            mappers = runai.models.mappers.Mappers(
                    gid = '', 
                    uid = '', 
                    groups = '', 
                    supplementary_groups = '', 
                    email = '', )
        )

        # Make the API call
        api_response = api_instance.create_idp(
            idp_creation_request=idp_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_idp: {e}")

def example_delete_idp():
    """
    Example of using delete_idp
    
    Delete external idp by alias
    
    """
    try:
        # Prepare the request parameters
        idp = "example_idp"
        
        
        
        
        
        
        

        # Make the API call
        api_instance.delete_idp(
            idp=idp,
        )

    except Exception as e:
        print(f"Exception when calling delete_idp: {e}")

def example_get_idp():
    """
    Example of using get_idp
    
    Get external idp by alias
    
    """
    try:
        # Prepare the request parameters
        idp = "example_idp"
        
        
        
        
        
        
        

        # Make the API call
        api_instance.get_idp(
            idp=idp,
        )

    except Exception as e:
        print(f"Exception when calling get_idp: {e}")

def example_get_idp_mappers():
    """
    Example of using get_idp_mappers
    
    Get idp mappers
    
    """
    try:
        # Prepare the request parameters
        idp = "example_idp"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_idp_mappers(
            idp=idp,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_idp_mappers: {e}")

def example_get_idps():
    """
    Example of using get_idps
    
    Get external idps list
    
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_idps()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_idps: {e}")

def example_update_idp():
    """
    Example of using update_idp
    
    Update external idp by alias
    
    """
    try:
        # Prepare the request parameters
        idp = "example_idp"
        
        
        
        
        
        
        
        
        # Create example data for IdpCreationRequest
        idp_creation_request = models.IdpCreationRequest(
            name = '',
            type = 'oidc',
            saml_data = runai.models.saml_creation_data.SamlCreationData(
                    metadata_xml_url = '', 
                    metadata_xml_file = '', 
                    file_name = '', 
                    metadata_xml_type = null, 
                    entity_id = '', ),
            oidc_data = runai.models.oidc_creation_data.OidcCreationData(
                    client_id = '0', 
                    client_secret = '0', 
                    discover_document_url = '', 
                    scopes = [
                        '0 JLe6iL71-aa-.Ctq:dcsc.3-8:1g 8Xa6u61ArrlGpCQjkQVRmfnjddwcDM.:fvlxVU:5mAsDwtJsoLm0U2Qzc bMGoFtYYnOi3Uynm7-iBPXDeXK7FerdNFRGYVtmAOl5_Cq2Rl4hC2QiYJ5AOF77DBqQaK90sLp4g4V9O-6o daJrr3kIA8m85_YUSTN-PJy8dgSQzlarQkEaQ7MSI_JXg0j7ljZfgn2bLVk .jh-SQfnnBmLmok4-qyj::FnMc c1s:zY.5cKhAX0a5bAbk48VRGGhVIVFbPoXoEqb1EjLwWHMEWwnY_Z2TcNg1eoeI:Sh..EKMforDc7IjMfFpU0 0osd6el-_scVo4.4LpdT7v:MWCKJ--bQ2llJ.xnhemZK2YEVOdfGqWVRaJTQ6NZjv7Fim84dl:6u:bf 1siac5xO36MmDLWjJ3jQlUx0EM7QTdbqkuy39oC5lk0tnyKSHbk-zevT:KaSOnxfj6h3vQb5v8wk6Sg8 5NDiQoZsM.l6i6i:X3nW1dw8EowTNIWEw9A9emf4X1K3ldM15JuA8a:fOZ9xEnRJanu0Ocoq2B7wgBww9rSjSF 04JADnYUXiaAascLalMZXWxP.coV3uIqL2NwG1Q15bVN8-C4QbrRP8xA 4fth0O_ATmjWCKOzvZrmHsFgm1BjNZgMZgeBXCspwU7tvy Rc4xEuKdFMjyAKR9T_PAefg3k17A:4:LQ0hCGa qQO7invEoLeDe-T2FaL5:Eugu9mSRm1:hhMc_fyRqSs6qs6m:6:uapkGM.emZJKhxxu.cSv4lgZIy39ZAP 183DZ6eFRHoCI32RZpIF1hrunoV2CN8hBG3asQY9si01no:Lr29sCi5fusnO0Pt9m_WBzmDQ.rY-.dWc8IoIfsOVxrxONEet:y2Ea2WBnlIeVDDvoQkWfnHqpzl38HSun:67NTGpyvcLUvLesddb7ZeMnxTiEdp3QB25:xPgTL:jsXt6AS-qWtRiUTSPvdeYfIa5D9W:m3zlielNqY57V5GNavSBLiBzZEK-XN5w5vzvhhxxZvZ6DSZk7t.Yolw3zR W54JVAgX5uBCBgOEU-0z8IvupQn1Ln7KN9-Rm8grr3yUXv8ymTkuKbSl:ey-0o3kDV _NwFlRcRlkQG052yAruvGoDsRGUWvpp1g3iLwXxMqtsSg-S-mz4inAC2m16mBnktro i:E.Q97mOyiQ-PlkSWd2vgJF_wnac2TI0P3OQpfYVThWWtT9C4EMdkEGXvo_pF8a LrcWJySttXG_L_wVcihNkaQVvG2k6.uK19A8bsb5bHBstV_iIURKFgWngEotMsNwFg4m4G2eGYR8Mev:ehM20oC Errt5WLpKogarQ79jUuJvoXzAALsnC:L2n9:1NrppKZo51WAYJ-O2VKkDZikuODyWW0miNkaUbJIKSGQz_mnaoCLSQ_OtCiGx2GBiVurYQU0 tHCmwy3_ZeZA8sXIqyMK5hfbO8CdOVIQ4-HWt1xfvGn3nycbCcB7ppl1xtGm tRB-edDfMd3SIbhyKQMLYa0D8SK2ROcYS6s8bD.Hj9Vrukx9 IXyLnTz6BL189TiKs1hzAmdz_H34DxOE1dqyOEzw2z:UfO6ZOCxGJIaF45I6qCx7vRzlOA:WVc:KzPhB40gB1s-q LQ6wRNld4ksNBvgoQbDSWwAEMIc3Lj1ZgSMD0kq10azd CNZotNqQMCcju5aZsU-.FOOCz1M6jYtjmzvGJFn2fomOLL_hhqKOV60ej4Wnb_Apr4Ii_830jhIct4_rnneTA ..ovWFYW.CDaz46v9mCKpToacUmuGfCXEgzBnP79sSBiK5J6DY2iFdET cuwWm5l6xJxLA1YFRqNFkORfSvLyHt-wefW4HUCgpVF5n7APxkF8Nq1-YWQXnC5Y0ywM6ra0fyPpof3VJr49NnQIM51BNoxsmnTY1739rkUGdgd74tjas0TsDj5wyogLbwq-uTK1ZSfODxfI5QrkOFgTfOJGSbCqcPFMR3oslc:vpXnLorh5IU6uq.kNtRBhdJpSG1krkOL5MnFWE4P0-orkSE61hbFzxTbuQc._CwA_cp-f8GTTep6KCSJfW.E6Zdi tN_1o.-93XmBlm1HhlFW2zKw5vRQCs.l8MU30wJ0Xu4zaw6ZBCeyDXp.35yLDHME3VQ4V9g8G vZOdS5Dqbe0Oq4p-3JFwIM265vdxXSEblrXLwsD56B1sm2fZZ_bSdPjKZMNe-SiE7E CF9R6igWguK38C-YraMyWtjI3LzdIwl LOrclq3ZeaFeS_cB.PcTw2F4.Qy9f7.THaGxysoJ79-Jh7_hh0aY28FE-hKazu2q3ZSgSxP7:.9sjse8DuY00860KstM44-0TNAtJJMpMKh7thZ37KQ6Yz45:EAe:eM:5ByDb:UF-H08dH6ENnOyK0rn-.7nj2o9.I JjhiBor6nvE2Bma7t5_0T9S.k.PlpeHxBZj_nZnSqrt8Q_3PmUNmV6ElLRzt6qdGD -o4ENqGg4sU2clcshSIKL6f91oYknUPgy9SzJ5 2e7VcTJR5lRaJ6vbt-w_u3bRL.UYuVHga1BZs1cGujVpFQPgZawqkh6Ol7Rhf8zYz2Xeit5C8Q.81Ud:PwaA8KCYLzw681h rzxd8cpSQSbF1dYbIr23c0snlZjFHRpfWGrvYTpIIGO-_9prQk6F6xlc91-JWKZiEs93TaiRpcNLUKhtKvojBba_NwfiM0TmNCT_Wkp6hZLEFsEMb.I3l9c9z8u.c5oyGUNrHqlgyf.jcM:bkOP-tqJCvg I:bROCxOuQxLs7.UmGqoYnGmxwAVq2LPLBRjKM0pRLkDCBlF07zgqZcklnDNngwtOv:uSEFxM7zrskU3J_r71Q-.y5y9CSqJeGnyzs.vV0JSlLRfIqIYN34uhQpQF3PP1fjnhOr1nrPls5PcefAlsQBVYpZYj j28vlhigAJFKibS0F8kjuosVcKs5ZG:-D9F:92L9szPZ5gwrK6vwUqPfmW:ud_3F3KPFTlwx0K.ebAlFsyge0khhbbtQky2yND:FHpXJGrZDg4L-ocNz9VaQlP1aglh-FZUr55YNHq:2W j4eBDEmkb1qqTVohVN_Dbai2Y9:GvIitIehfcfMBzd.VfZRyMhl.0_oJ5qXd:0syO1bg2ZOdgkHncAMCg9fGsrVMyvqQPW1:6GtR8z1T7hDB1lNwHA:APHxC3CnVD:h0mztR8Ede_n8uuQ5QEd0.O60APIr045S3a1qyOCZORhPNuZQZUR8zEN_mU2ASTYnh0nT411-0q2zinWNpU3sfPF6d3i1uHRJu1ll6NxtpA2yX7fHQ kYJ0E5A2DP6EkHbyU6Vhy_cCMi.LQ7:yW.l2OPU9btfLxZay-AzzqWyVtoW:YDpEXdX3W1Qs7ExXxH6sgXc-B: sllDaUUdPbtWRpkAd327lBy30Vu8Ms9Gt.Vg5PyuLUXwlXx2-Kdl5o7cZmGK32rd0iJZduxLYd6I0NZhmQod7LeZOTLbSB1D1N-2q0NaV8.B4Z6YH2XxHb5INP2m:lK4:9UVwsYYkC:jCzRvoh FYL1 :0tF.6qtuVKEwSIfN2z52zDVxOyJK2UhLLVF1-EjuwmkUZ_lJQG32Al392JxPtH_IWdzEVTBbaU68dh_YVTqN-SYh263UL1kK xb9EvP8QzfbIXzsncvZ_3cFFflBDN5SlsWvgnHaPQ8lC94xmtsePqTu3fpMHEAPabvJF'
                        ], 
                    mandatory_claim = {values=[Ljava.lang.Object;@625487a6, claim=claim}, ),
            ocp_data = runai.models.ocp_creation_data.OcpCreationData(
                    client_id = '0', 
                    idp_base_url = '', 
                    client_secret = '0', 
                    scopes = [
                        '0 JLe6iL71-aa-.Ctq:dcsc.3-8:1g 8Xa6u61ArrlGpCQjkQVRmfnjddwcDM.:fvlxVU:5mAsDwtJsoLm0U2Qzc bMGoFtYYnOi3Uynm7-iBPXDeXK7FerdNFRGYVtmAOl5_Cq2Rl4hC2QiYJ5AOF77DBqQaK90sLp4g4V9O-6o daJrr3kIA8m85_YUSTN-PJy8dgSQzlarQkEaQ7MSI_JXg0j7ljZfgn2bLVk .jh-SQfnnBmLmok4-qyj::FnMc c1s:zY.5cKhAX0a5bAbk48VRGGhVIVFbPoXoEqb1EjLwWHMEWwnY_Z2TcNg1eoeI:Sh..EKMforDc7IjMfFpU0 0osd6el-_scVo4.4LpdT7v:MWCKJ--bQ2llJ.xnhemZK2YEVOdfGqWVRaJTQ6NZjv7Fim84dl:6u:bf 1siac5xO36MmDLWjJ3jQlUx0EM7QTdbqkuy39oC5lk0tnyKSHbk-zevT:KaSOnxfj6h3vQb5v8wk6Sg8 5NDiQoZsM.l6i6i:X3nW1dw8EowTNIWEw9A9emf4X1K3ldM15JuA8a:fOZ9xEnRJanu0Ocoq2B7wgBww9rSjSF 04JADnYUXiaAascLalMZXWxP.coV3uIqL2NwG1Q15bVN8-C4QbrRP8xA 4fth0O_ATmjWCKOzvZrmHsFgm1BjNZgMZgeBXCspwU7tvy Rc4xEuKdFMjyAKR9T_PAefg3k17A:4:LQ0hCGa qQO7invEoLeDe-T2FaL5:Eugu9mSRm1:hhMc_fyRqSs6qs6m:6:uapkGM.emZJKhxxu.cSv4lgZIy39ZAP 183DZ6eFRHoCI32RZpIF1hrunoV2CN8hBG3asQY9si01no:Lr29sCi5fusnO0Pt9m_WBzmDQ.rY-.dWc8IoIfsOVxrxONEet:y2Ea2WBnlIeVDDvoQkWfnHqpzl38HSun:67NTGpyvcLUvLesddb7ZeMnxTiEdp3QB25:xPgTL:jsXt6AS-qWtRiUTSPvdeYfIa5D9W:m3zlielNqY57V5GNavSBLiBzZEK-XN5w5vzvhhxxZvZ6DSZk7t.Yolw3zR W54JVAgX5uBCBgOEU-0z8IvupQn1Ln7KN9-Rm8grr3yUXv8ymTkuKbSl:ey-0o3kDV _NwFlRcRlkQG052yAruvGoDsRGUWvpp1g3iLwXxMqtsSg-S-mz4inAC2m16mBnktro i:E.Q97mOyiQ-PlkSWd2vgJF_wnac2TI0P3OQpfYVThWWtT9C4EMdkEGXvo_pF8a LrcWJySttXG_L_wVcihNkaQVvG2k6.uK19A8bsb5bHBstV_iIURKFgWngEotMsNwFg4m4G2eGYR8Mev:ehM20oC Errt5WLpKogarQ79jUuJvoXzAALsnC:L2n9:1NrppKZo51WAYJ-O2VKkDZikuODyWW0miNkaUbJIKSGQz_mnaoCLSQ_OtCiGx2GBiVurYQU0 tHCmwy3_ZeZA8sXIqyMK5hfbO8CdOVIQ4-HWt1xfvGn3nycbCcB7ppl1xtGm tRB-edDfMd3SIbhyKQMLYa0D8SK2ROcYS6s8bD.Hj9Vrukx9 IXyLnTz6BL189TiKs1hzAmdz_H34DxOE1dqyOEzw2z:UfO6ZOCxGJIaF45I6qCx7vRzlOA:WVc:KzPhB40gB1s-q LQ6wRNld4ksNBvgoQbDSWwAEMIc3Lj1ZgSMD0kq10azd CNZotNqQMCcju5aZsU-.FOOCz1M6jYtjmzvGJFn2fomOLL_hhqKOV60ej4Wnb_Apr4Ii_830jhIct4_rnneTA ..ovWFYW.CDaz46v9mCKpToacUmuGfCXEgzBnP79sSBiK5J6DY2iFdET cuwWm5l6xJxLA1YFRqNFkORfSvLyHt-wefW4HUCgpVF5n7APxkF8Nq1-YWQXnC5Y0ywM6ra0fyPpof3VJr49NnQIM51BNoxsmnTY1739rkUGdgd74tjas0TsDj5wyogLbwq-uTK1ZSfODxfI5QrkOFgTfOJGSbCqcPFMR3oslc:vpXnLorh5IU6uq.kNtRBhdJpSG1krkOL5MnFWE4P0-orkSE61hbFzxTbuQc._CwA_cp-f8GTTep6KCSJfW.E6Zdi tN_1o.-93XmBlm1HhlFW2zKw5vRQCs.l8MU30wJ0Xu4zaw6ZBCeyDXp.35yLDHME3VQ4V9g8G vZOdS5Dqbe0Oq4p-3JFwIM265vdxXSEblrXLwsD56B1sm2fZZ_bSdPjKZMNe-SiE7E CF9R6igWguK38C-YraMyWtjI3LzdIwl LOrclq3ZeaFeS_cB.PcTw2F4.Qy9f7.THaGxysoJ79-Jh7_hh0aY28FE-hKazu2q3ZSgSxP7:.9sjse8DuY00860KstM44-0TNAtJJMpMKh7thZ37KQ6Yz45:EAe:eM:5ByDb:UF-H08dH6ENnOyK0rn-.7nj2o9.I JjhiBor6nvE2Bma7t5_0T9S.k.PlpeHxBZj_nZnSqrt8Q_3PmUNmV6ElLRzt6qdGD -o4ENqGg4sU2clcshSIKL6f91oYknUPgy9SzJ5 2e7VcTJR5lRaJ6vbt-w_u3bRL.UYuVHga1BZs1cGujVpFQPgZawqkh6Ol7Rhf8zYz2Xeit5C8Q.81Ud:PwaA8KCYLzw681h rzxd8cpSQSbF1dYbIr23c0snlZjFHRpfWGrvYTpIIGO-_9prQk6F6xlc91-JWKZiEs93TaiRpcNLUKhtKvojBba_NwfiM0TmNCT_Wkp6hZLEFsEMb.I3l9c9z8u.c5oyGUNrHqlgyf.jcM:bkOP-tqJCvg I:bROCxOuQxLs7.UmGqoYnGmxwAVq2LPLBRjKM0pRLkDCBlF07zgqZcklnDNngwtOv:uSEFxM7zrskU3J_r71Q-.y5y9CSqJeGnyzs.vV0JSlLRfIqIYN34uhQpQF3PP1fjnhOr1nrPls5PcefAlsQBVYpZYj j28vlhigAJFKibS0F8kjuosVcKs5ZG:-D9F:92L9szPZ5gwrK6vwUqPfmW:ud_3F3KPFTlwx0K.ebAlFsyge0khhbbtQky2yND:FHpXJGrZDg4L-ocNz9VaQlP1aglh-FZUr55YNHq:2W j4eBDEmkb1qqTVohVN_Dbai2Y9:GvIitIehfcfMBzd.VfZRyMhl.0_oJ5qXd:0syO1bg2ZOdgkHncAMCg9fGsrVMyvqQPW1:6GtR8z1T7hDB1lNwHA:APHxC3CnVD:h0mztR8Ede_n8uuQ5QEd0.O60APIr045S3a1qyOCZORhPNuZQZUR8zEN_mU2ASTYnh0nT411-0q2zinWNpU3sfPF6d3i1uHRJu1ll6NxtpA2yX7fHQ kYJ0E5A2DP6EkHbyU6Vhy_cCMi.LQ7:yW.l2OPU9btfLxZay-AzzqWyVtoW:YDpEXdX3W1Qs7ExXxH6sgXc-B: sllDaUUdPbtWRpkAd327lBy30Vu8Ms9Gt.Vg5PyuLUXwlXx2-Kdl5o7cZmGK32rd0iJZduxLYd6I0NZhmQod7LeZOTLbSB1D1N-2q0NaV8.B4Z6YH2XxHb5INP2m:lK4:9UVwsYYkC:jCzRvoh FYL1 :0tF.6qtuVKEwSIfN2z52zDVxOyJK2UhLLVF1-EjuwmkUZ_lJQG32Al392JxPtH_IWdzEVTBbaU68dh_YVTqN-SYh263UL1kK xb9EvP8QzfbIXzsncvZ_3cFFflBDN5SlsWvgnHaPQ8lC94xmtsePqTu3fpMHEAPabvJF'
                        ], ),
            mappers = runai.models.mappers.Mappers(
                    gid = '', 
                    uid = '', 
                    groups = '', 
                    supplementary_groups = '', 
                    email = '', )
        )

        # Make the API call
        api_instance.update_idp(
            idp=idp,
            idp_creation_request=idp_creation_request,
        )

    except Exception as e:
        print(f"Exception when calling update_idp: {e}")

def example_update_idp_mappers():
    """
    Example of using update_idp_mappers
    
    Update idp mappers
    
    """
    try:
        # Prepare the request parameters
        idp = "example_idp"
        
        
        
        
        
        
        
        
        # Create example data for Mappers
        mappers = models.Mappers(
            gid = '',
            uid = '',
            groups = '',
            supplementary_groups = '',
            email = ''
        )

        # Make the API call
        api_instance.update_idp_mappers(
            idp=idp,
            mappers=mappers,
        )

    except Exception as e:
        print(f"Exception when calling update_idp_mappers: {e}")

