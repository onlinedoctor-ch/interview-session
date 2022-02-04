import {Config} from './config';

interface DoctorBase {
  first_name: string;
  last_name: string;
  specialization: string;
}

export interface Doctor extends DoctorBase {
  id: number;
}

export interface DoctorCreate extends DoctorBase {}


export async function getDoctors() {
  const response = await fetch(`${Config.apiBaseUrl}doctors`);
  if (response.status !== 200) {
    throw new Error(`Api Request failed with status: ${response.status}`);
  }
  return response.json();
}

export async function createDoctor(doctor: DoctorCreate) {
  const response = await fetch(`${Config.apiBaseUrl}doctors`, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(doctor),
  });
  if (response.status !== 201) {
    throw new Error(`Api Request failed with status: ${response.status}`);
  }
  return response.json();
}

export async function deleteDoctor(doctorId: number) {
  const response = await fetch(`${Config.apiBaseUrl}doctors/${doctorId}`, {
    method: "delete",
  });
  if (response.status !== 200) {
    throw new Error(`Api Request failed with status: ${response.status}`);
  }
  return response.json();
}
