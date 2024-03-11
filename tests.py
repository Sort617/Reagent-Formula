@test.describe('Basic Tests')
def basic_tests():

    @test.it("It should works for basic tests.")
    def basic_test_cases():
            
        test.assert_equals(isValid([1,3,7]),True)
        
        test.assert_equals(isValid([7,1,2,3]),False)
        
        test.assert_equals(isValid([1,3,5,7]),False)
        
        test.assert_equals(isValid([1,5,6,7,3]),True)
        
        test.assert_equals(isValid([5,6,7]),True)
        
        test.assert_equals(isValid([5,6,7,8]),True)
        
        test.assert_equals(isValid([6,7,8]),False)
        
        test.assert_equals(isValid([7,8]),True)
