using UnityEngine;

public class VRController : MonoBehaviour
{
    void Start()
    {
        Debug.Log("VR Controller Initialized");
    }

    void Update()
    {
        if (Input.GetButtonDown("Fire1"))
        {
            Debug.Log("VR Action triggered");
        }
    }
}
