import time
import pytest
from FrameWork.peza.peza_execution_plan.berms_execution_plan import BermsExecutionPlanExcelRead
from FrameWork.peza.peza_execution_plan.sign_up_execution_plan import SignUpExecutionPlanExcelRead
from FrameWork.peza.peza_execution_plan.ecai_execution_plan import ECAIExecutionPlanExcelRead
from FrameWork.peza.peza_execution_plan.import_permit_execution_plan import ImporterPermitExecutionPlanExcelRead
from FrameWork.ECP.ecp_execution_scripts.ecp_sign_up_execution_plan import ecpExecutionPlanExcelRead


# @pytest.mark.usefixtures("setup")
# class TestPezaSignup01:
#     def test_new_sign_up_enterprise(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - Sign-up Enterprise - SolePro.xlsx")
#         time.sleep(5)
#
#     def test_new_sign_up_enterprise(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - Sign-up Enterprise - Partnership.xlsx")
#         time.sleep(5)
#
#     def test_new_sign_up_enterprise(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - Sign-up Enterprise - Corporation.xlsx")
#         time.sleep(5)
#
#     def test_new_sign_up_enterprise(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - Sign-up Enterprise - Cooperative.xlsx")
#         time.sleep(5)

#     def test_new_sign_up_developer(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - Sign-up Developer.xlsx")
#         time.sleep(5)

#     def test_new_sign_up_others_non_peza(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - Sign-up Others Non-PEZA.xlsx")
#         time.sleep(5)

# @pytest.mark.usefixtures("setup")
# class TestPezaSignup03:
#     def test_new_sign_up_service_provider(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.2 - Sign-up SP.xlsx")
#         time.sleep(5)

# @pytest.mark.usefixtures("setup")
# class TestPezaECAITestCase:
#     def test_new_sign_up_service_provider(self):
#         planned_test_execution = ECAIExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20240702_PEZA_CPF_v1.1 - ECAI Developer.xlsx")
#         time.sleep(5)

# @pytest.mark.usefixtures("setup")
# class TestPezaSignupSPTestCase:
#     def test_new_sign_up_service_provider_01(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\Multiple File\20231130_PEZA_CPF_v1.2 - Sign-up SP 1.xlsx")
#
#     def test_new_sign_up_service_provider_02(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\Multiple File\20231130_PEZA_CPF_v1.2 - Sign-up SP 2.xlsx")
#
#     def test_new_sign_up_service_provider_03(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\Multiple File\20231130_PEZA_CPF_v1.2 - Sign-up SP 3.xlsx")
#
#     def test_new_sign_up_service_provider_04(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\Multiple File\20231130_PEZA_CPF_v1.2 - Sign-up SP 4.xlsx")
#
#     def test_new_sign_up_service_provider_05(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\Multiple File\20231130_PEZA_CPF_v1.1 - Sign-up SP 05.xlsx")
#
#     def test_new_sign_up_service_provider_06(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\Multiple File\20231130_PEZA_CPF_v1.1 - Sign-up SP 06.xlsx")
#
#     def test_new_sign_up_service_provider_07(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\Multiple File\20231130_PEZA_CPF_v1.1 - Sign-up SP 07.xlsx")
#
#     def test_new_sign_up_service_provider_08(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\Multiple File\20231130_PEZA_CPF_v1.1 - Sign-up SP 08.xlsx")
#
#     def test_new_sign_up_service_provider_09(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\Multiple File\20231130_PEZA_CPF_v1.1 - Sign-up SP 09.xlsx")
#
#     def test_new_sign_up_service_provider_10(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\Multiple File\20231130_PEZA_CPF_v1.1 - Sign-up SP 10.xlsx")
#
#     def test_new_sign_up_service_provider_11(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\Multiple File\20231130_PEZA_CPF_v1.1 - Sign-up SP 11.xlsx")
#
#     def test_new_sign_up_service_provider_all(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - Sign-up SP all.xlsx")
#         time.sleep(5)
#
#     def test_new_sign_up_service_provider_all_approve(self):
#         planned_test_execution = SignUpExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.2 - Sign-up SP - Approved All.xlsx")
#         time.sleep(5)

# @pytest.mark.usefixtures("setup")
# class TestPezaBermsTestCase1:
#     def test_developer_new_berms_01(self):
#         planned_test_execution = BermsExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.3 - BERMS Developer 1.xlsx")
#         time.sleep(5)
#
#     def test_developer_new_berms_02(self):
#         planned_test_execution = BermsExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.3 - BERMS Developer 2.1.xlsx")
#         time.sleep(5)

# @pytest.mark.usefixtures("setup")
# class TestPezaBermsTestCase2:
#     def test_enterprise_new_berms(self):
#         planned_test_execution = BermsExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - BERMS Enterprise New.xlsx")
#         time.sleep(5)

@pytest.mark.usefixtures("setup")
class TestPezaBermsTestCase3:
    def test_enterprise_new_berms_new_signup(self):
        planned_test_execution = BermsExecutionPlanExcelRead(self.driver)
        planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - BERMS Enterprise New - New Sign up.xlsx")
        time.sleep(5)

# @pytest.mark.usefixtures("setup")
# class TestPezaBermsTestCase3:
#     def test_enterprise_amendment_berms(self):
#         planned_test_execution = BermsExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - BERMS Enterprise Amendment.xlsx")
#         time.sleep(5)

# @pytest.mark.usefixtures("setup")
# class TestPezaBermsTestCase4:
#     def test_enterprise_new_project_berms(self):
#         planned_test_execution = BermsExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - BERMS Enterprise New Project.xlsx")
#         time.sleep(5)

# @pytest.mark.usefixtures("setup")
# class TestPezaBermsTestCase5:
#     def test_enterprise_expansion_berms(self):
#         planned_test_execution = BermsExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - BERMS Enterprise Expansion.xlsx")
#         time.sleep(5)

# @pytest.mark.usefixtures("setup")
# class TestPezaBermsTestCase6:
#     def test_service_provider_air_freight_forwader(self):
#         planned_test_execution = BermsExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - BERMS SP SFF.xlsx")
#
#     def test_service_provider_air_freight_forwader(self):
#         planned_test_execution = BermsExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - BERMS SP AFF.xlsx")
#
#     def test_service_provider_truck_hauling(self):
#         planned_test_execution = BermsExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - BERMS SP Truck Hauling.xlsx")
#
#     def test_service_provider_security_agency(self):
#         planned_test_execution = BermsExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - BERMS SP Security Agency.xlsx")
#
#     def test_service_provider_customs_broker(self):
#         planned_test_execution = BermsExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20231130_PEZA_CPF_v1.1 - BERMS SP Customs Broker.xlsx")
#         time.sleep(5)

# @pytest.mark.usefixtures("setup")
# class TestPezaBermsApprovalTestCase2:
#     def test_enterprise_new_berms(self):
#         planned_test_execution = BermsExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20240703_PEZA_CPF_v1.1 - BERMS Enterprise - Approval.xlsx")
#         time.sleep(5)
#
#     def test_enterprise_new_berms(self):
#         planned_test_execution = BermsExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20240703_PEZA_CPF_v1.2 - BERMS Enterprise - Approval.xlsx")
#         time.sleep(5)

# @pytest.mark.usefixtures("setup")
# class TestImportPermitTestCase01:
#     def test_enterprise_new_import_permit(self):
#         planned_test_execution = ImporterPermitExecutionPlanExcelRead(self.driver)
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\PEZA CP\20240827_PEZA_CPF_v1.1 - IP Enterprise.xlsx")
#         time.sleep(5)

# @pytest.mark.usefixtures("ecp_setup")
# class TestECPTestCase:
#     def test_developer_new_berms(self):
#         planned_test_execution = ecpExecutionPlanExcelRead(self.driver)
#         # planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\ECP\20240403_ECP - sign_up v1.0.xlsx")
#         planned_test_execution.test_execution_plan_read_excel(r"C:\Scripts\ECP\20240403_ECP - ECP Application v1.0.xlsx")
#         time.sleep(5)