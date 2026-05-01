import { createAsyncThunk, createSlice, PayloadAction } from "@reduxjs/toolkit";
import { loginService } from "./service";
import { LoginRequest, AuthState } from "./type";

const initialState: AuthState = {
  accessToken: null,
  refreshToken: null,
  isAuthenticated: false,
  loading: false,
  error: null,
};

export const authUser = createAsyncThunk(
  "auth/user",
  async (payload: LoginRequest, { rejectWithValue }) => {
    try {
      const data = await loginService(payload);
      return data;
    } catch (err: any) {
      return rejectWithValue(err.response?.data || "Login failed");
    }
  }
);

const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    setLoading(state, action: PayloadAction<boolean>) {
      state.loading = action.payload;
    },

    setError(state, action: PayloadAction<string | null>) {
      state.error = action.payload;
      state.loading = false;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(authUser.pending, (state) => {
        state.loading = true;
        state.isAuthenticated = false;
        state.error = null;
      })
      .addCase(authUser.fulfilled, (state, action) => {
        state.loading = false;
        state.accessToken = action.payload.access;
        state.refreshToken = action.payload.refresh;
        state.isAuthenticated = true;
        state.error = null;
      })
      .addCase(authUser.rejected, (state) => {
        state.loading = false;
        state.isAuthenticated = false;
        state.error = "Login failed";
      });
  },
});

export const { setLoading, setError } = authSlice.actions;

export default authSlice.reducer;