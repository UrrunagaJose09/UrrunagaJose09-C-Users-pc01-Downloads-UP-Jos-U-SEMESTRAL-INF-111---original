import prg1, prg2, prg3, prg4, prg5, prg6, prg7, prg8, prg9, prg10
import prg11, prg12, prg13, prg14, prg15, prg16, prg17, prg18, prg19, prg20
import prg21, prg22, prg23, prg24, prg25, prg26, prg27, prg28, prg29, prg30
import prg31, prg32, prg33, prg34, prg35, prg36, prg37, prg38, prg39, prg40
import prg41, prg42, prg43, prg44, prg45, prg46, prg47, prg48, prg49, prg50
import time

def Semestral():
    while True:
        print("\n")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                     ==== Menú ====                       ║")
        print("║                                                          ║")
        print("║   1. Ejecutar prg1        11. Ejecutar prg11             ║")
        print("║   2. Ejecutar prg2        12. Ejecutar prg12             ║")
        print("║   3. Ejecutar prg3        13. Ejecutar prg13             ║")
        print("║   4. Ejecutar prg4        14. Ejecutar prg14             ║")
        print("║   5. Ejecutar prg5        15. Ejecutar prg15             ║")
        print("║   6. Ejecutar prg6        16. Ejecutar prg16             ║")
        print("║   7. Ejecutar prg7        17. Ejecutar prg17             ║")
        print("║   8. Ejecutar prg8        18. Ejecutar prg18             ║")
        print("║   9. Ejecutar prg9        19. Ejecutar prg19             ║")
        print("║  10. Ejecutar prg10       20. Ejecutar prg20             ║")
        print("║                                                          ║")
        print("║  21. Ejecutar prg21       31. Ejecutar prg31             ║")
        print("║  22. Ejecutar prg22       32. Ejecutar prg32             ║")
        print("║  23. Ejecutar prg23       33. Ejecutar prg33             ║")
        print("║  24. Ejecutar prg24       34. Ejecutar prg34             ║")
        print("║  25. Ejecutar prg25       35. Ejecutar prg35             ║")
        print("║  26. Ejecutar prg26       36. Ejecutar prg36             ║")
        print("║  27. Ejecutar prg27       37. Ejecutar prg37             ║")
        print("║  28. Ejecutar prg28       38. Ejecutar prg38             ║")
        print("║  29. Ejecutar prg29       39. Ejecutar prg39             ║")
        print("║  30. Ejecutar prg30       40. Ejecutar prg40             ║")
        print("║                                                          ║")
        print("║  41. Ejecutar prg41       46. Ejecutar prg46             ║")
        print("║  42. Ejecutar prg42       47. Ejecutar prg47             ║")
        print("║  43. Ejecutar prg43       48. Ejecutar prg48             ║")
        print("║  44. Ejecutar prg44       49. Ejecutar prg49             ║")
        print("║  45. Ejecutar prg45       50. Ejecutar prg50             ║")
        print("║                                                          ║")
        print("║                                                          ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print("********** PRESIONE q PARA SALIR **********")

        choice = input("Elige una opción: ").strip().lower()
        print("\n")
        match choice:
            case "1":
                prg1.sum_n()
            case "2":
                prg2.impuesto_p()
            case "3":
                prg3.area_r()
            case "4":
                prg4.perimetro_r()
            case "5":
                prg5.trapecio_ar()
            case "6":
                prg6.volomen_rec()
            case "7":
                prg7.valor_()
            case "8":
                prg8.salario_xh()
            case "9":
                prg9.des_p()
            case "10":
                prg10.conver_t()
            case "11":
                prg11.num_1x0()
            case "12":
                prg12.person_ad()
            case "13":
                prg13.mult_5()
            case "14":
                prg14.deter_v()
            case "15":
                prg15.verif_5()
            case "16":
                prg16.clasfic_edad()
            case "17":
                prg17.cal_des_if()
            case "18":
                prg18.verif_rang()
            case "19":
                prg19.dtrg_l_d()
            case "20":
                prg20.num_comprr()
            case "21":
                prg21.num_prim()
            case "22":
                prg22.net_salar()
            case "23":
                prg23.sigl_deter()
            case "24":
                prg24.trian_verefic()
            case "25":
                prg25.trab_catg()
            case "26":
                prg26.Imc_clas()
            case "27":
                prg27.licenc_deter()
            case "28":
                prg28.divs_3_5_deter()
            case "29":
                prg29.name_verif()
            case "30":
                prg30.tarif_tax()
            case "31":
                prg31.sumnum_wh()
            case "32":
                prg32.contr_num()
            case "33":
                prg33.sumar_limit()
            case "34":
                prg34.sumar_digit()
            case "35":
                prg35.adivi_num()
            case "36":
                prg36.multip_num()
            case "37":
                prg37.valid_Ent()
            case "38":
                prg38.cont_digit()
            case "39":
                prg39.binar_conver()
            case "40":
                prg40.cajer_simulator()
            case "41":
                prg41.tabl_mult()
            case "42":
                prg42.sumar_numpares()
            case "43":
                prg43.vocal_cont()
            case "44":
                prg44.num_imprim()
            case "45":
                prg45.imprimr_impares()
            case "46":
                prg46.sumar_numnatural()
            case "47":
                prg47.num_deterprim()
            case "48":
                prg48.cel_and_fhtr_conver()
            case "49":
                prg49.draw_triang()
            case "50":
                prg50.repit_cadm()
            case "q":
                print("\n")
                print("╔═════════════════════════════════════════════════════════════════╗")
                print("║                                                                 ║")
                print("║ Semestral Presentado por: José Urrunaga y Eydan Trujillo        ║")
                print("║                                                                 ║")
                print("╚═════════════════════════════════════════════════════════════════╝")
                print("\n")
                print("Saliendo...")
                break
            case _:
                print("Opción no válida, intenta de nuevo.")
        
        
        time.sleep(6)

if __name__ == "__main__":
    Semestral()
