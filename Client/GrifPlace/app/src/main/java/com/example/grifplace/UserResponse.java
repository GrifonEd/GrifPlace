package com.example.grifplace;

import java.math.BigInteger;

public class UserResponse {
    private  String passport_number;
    private String first_name;
    private  String second_name;
    private String phone_number;
    private String password;

    public String getPassport_number() {
        return passport_number;
    }

    public void setPassport_number(String passport_number) {
        this.passport_number = passport_number;
    }

    public String getFirst_name() {
        return first_name;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public void setFirst_name(String first_name) {
        this.first_name = first_name;
    }

    @Override
    public String toString() {
        return "{" +
                "passport_number=" + passport_number +
                ", first_name='" + first_name + '\'' +
                ", second_name='" + second_name + '\'' +
                ", phone_number=" + phone_number + '\''+
                ", password=" + password + '\'' +
                '}';
    }

    public String getSecond_name() {
        return second_name;
    }

    public void setSecond_name(String second_name) {
        this.second_name = second_name;
    }

    public String getPhone_number() {
        return phone_number;
    }

    public void setPhone_number(String phone_number) {
        this.phone_number = phone_number;
    }
}
