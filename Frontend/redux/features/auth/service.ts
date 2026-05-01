import axiosInstance from "@/redux/api/axiosInstance";
import { LoginRequest, LoginResponse } from "./type";

export async function loginService(
  data: LoginRequest
): Promise<LoginResponse> {
  const response = await axiosInstance.post("/token/", data);
  return response.data;
}