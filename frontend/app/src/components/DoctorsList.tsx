import * as React from "react";
import { Button, Flex, Heading, useDisclosure } from "@chakra-ui/react";
import { Doctor, getDoctors, deleteDoctor } from "./doctorApi";
import { CreateDoctorModal } from "./CreateDoctorModal";

type PromiseState =
  | { status: "initial" }
  | { status: "loading" }
  | { status: "successfull"; data: Doctor[] }
  | { status: "failed"; error: string };

export const DoctorsList: React.FC = () => {
  const [requestState, setRequestState] = React.useState<PromiseState>({
    status: "initial",
  });
  const {
    isOpen: isCreationDialogOpen,
    onOpen: onOpenCreationDialog,
    onClose: onCloseCreationDialog,
  } = useDisclosure();

  const loadDoctors = async () => {
    setRequestState({ status: "loading" });
    try {
      const response = await getDoctors();
      setRequestState({ status: "successfull", data: response });
    } catch (error) {
      setRequestState({ status: "failed", error: error });
    }
  };

  React.useEffect(() => {
    loadDoctors();
  }, []);

  const onCloseDialog = () => {
    onCloseCreationDialog();
    loadDoctors();
  };

  return (
    <>
      <CreateDoctorModal
        isOpen={isCreationDialogOpen}
        onClose={onCloseDialog}
      />
      <Flex
        flexDir="row"
        justifyContent="space-between"
        alignItems="flex-end"
        mb={2}
      >
        <Heading size="md">Doctors</Heading>
        <Button onClick={onOpenCreationDialog}>Add Doctor</Button>
      </Flex>

      {requestState.status === "loading" && <span>Loading doctors...</span>}
      {requestState.status === "failed" && (
        <span>{requestState.error.toString()}</span>
      )}
      {requestState.status === "successfull" && (
        <Flex flexDirection="column" overflowY="auto">
          {requestState.data.map((doctor) => (
            <Flex
              key={doctor.id}
              flexDir="row"
              p={4}
              my={2}
              borderRadius={10}
              border="1px solid lightblue"
              justifyContent="space-between"
            >
              <Flex flexDir="column">
                <Heading size="sm">
                  {doctor.first_name} {doctor.last_name}
                </Heading>
                <Flex flexDir="row">{doctor.specialization}</Flex>
              </Flex>
              <Button
                onClick={async () => {
                  await deleteDoctor(doctor.id);
                  loadDoctors();
                }}
              >
                Delete
              </Button>
            </Flex>
          ))}
        </Flex>
      )}
    </>
  );
};
