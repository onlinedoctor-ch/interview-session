import * as React from "react";
import {
  Button,
  Input,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
} from "@chakra-ui/react";
import { Form, Formik } from "formik";
import { createDoctor } from "./doctorApi";

interface Props {
  isOpen: boolean;
  onClose: () => void;
}

export const CreateDoctorModal: React.FC<Props> = ({ isOpen, onClose }) => (
  <Modal isOpen={isOpen} onClose={onClose}>
    <ModalOverlay />
    <ModalContent>
      <ModalHeader>Create Doctor</ModalHeader>
      <ModalCloseButton />
      <Formik
        initialValues={{
          first_name: "",
          last_name: "",
          specialization: "",
        }}
        onSubmit={async (values) => {
          await createDoctor(values);
          onClose();
        }}
      >
        {({ values, handleChange, isSubmitting }) => (
          <Form>
            <ModalBody>
              <Input
                my={2}
                name="first_name"
                placeholder="First Name"
                value={values.first_name}
                onChange={handleChange}
              />
              <Input
                my={2}
                name="last_name"
                placeholder="Last Name"
                value={values.last_name}
                onChange={handleChange}
              />
              <Input
                my={2}
                name="specialization"
                placeholder="Specialization"
                value={values.specialization}
                onChange={handleChange}
              />
            </ModalBody>
            <ModalFooter>
              <Button
                mt={4}
                colorScheme="teal"
                isLoading={isSubmitting}
                type="submit"
              >
                Submit
              </Button>
            </ModalFooter>
          </Form>
        )}
      </Formik>
    </ModalContent>
  </Modal>
);
